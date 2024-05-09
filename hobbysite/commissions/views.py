from contextlib import redirect_stderr
from typing import Any
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Sum

from .models import Commission, Job, JobApplication
from .forms import CommissionForm, JobFormSet ,JobApplicationForm 


class CommissionsListView(ListView):
    model = Commission
    template_name = 'commissions_list.html'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['my_commissions'] = Commission.objects.filter(author=self.request.user.profile)
            context['commissions_applied'] = JobApplication.objects.filter(applicant = self.request.user.profile)
        return context

class CommissionsDetailView(DetailView):
    model = Commission
    form_class = JobApplicationForm()
    template_name = 'commissions_detail.html'
    

    def get_context_data(self, **kwargs):
        commission = self.get_object()
        context = super(CommissionsDetailView, self).get_context_data(**kwargs)
        jobs = Job.objects.filter(commission=commission)
        total_manpower_required = jobs.aggregate(total_manpower=Sum('manpower_required'))['total_manpower'] or 0
        total_accepted_applicants = JobApplication.objects.filter(job__in=jobs, status="2").count()
        open_manpower = total_manpower_required - total_accepted_applicants

        context['edit'] = self.request.user == commission.author
        context['commission'] = commission
        context['jobs'] = jobs
        context['total_manpower_required'] = total_manpower_required
        context['total_accepted_applicants'] = total_accepted_applicants
        context['open_manpower'] = open_manpower
        context['job_application_form'] = JobApplicationForm()
        return context
    

    def post(self, request, *args, **kwargs):
        self.object = self.get_object() # gets the Commission object
        job_application_form = JobApplicationForm(request.POST)
        job_application_form.fields['job'].queryset = Job.objects.filter(commission=self.object)
        if job_application_form.is_valid():
            job_application = job_application_form.save(commit=False) # create commission object but does not save
            job_application.commission = self.object
            job_application.applicant = self.request.user.profile
            job_application.save()
            return redirect('commissions:commissions')
        else:
            return self.render_to_response(self.get_context_data(form=job_application_form))
        

class CommissionsJobCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    template_name = 'commissions_create.html'
    fields = ['title', 'description', 'status']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['commission_form'] = CommissionForm(self.request.POST)
            context['job_formset'] = JobFormSet(self.request.POST)
        else:
            context['commission_form'] = CommissionForm()
            context['job_formset'] = JobFormSet()
        return context


    def form_valid(self, form):
        commission = form.save(commit=False) # create commission object but does not save
        commission.author = self.request.user.profile
        commission.save()
        context = self.get_context_data()
        job_formset = context['job_formset']
        if job_formset.is_valid():
            self.object = form.save()
            job_formset.instance = self.object
            job_formset.save()
        else:
            return self.render_to_response(self.get_context_data(form=form))
        return super().form_valid(form)
       

class CommissionsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Commission
    template_name = 'commissions_update.html'
    form_class = CommissionForm

    def test_func(self):
        obj = self.request.user.profile
        return obj.user == self.request.user
    
    def form_valid(self, form):
        form.instance.job = self.get_object()
        commission = form.save(commit=False) # create commission object but does not save
        # jobs = Job.objects.filter(commission=commission)
        print(commission.status)
        if all(job.status == '2' for job in Job.commission.objects.all()):
            commission.status = '2'
            print('status full')
        else:
            print('no')
        # for job in jobs:
        #     if job.status == '2':
        #         var += 1
        #         if var == total_manpower_required
        # if all(Job.objects.get(status='2')):
        #     commission.status = 2
        commission.save()
        
        return super().form_valid(form)