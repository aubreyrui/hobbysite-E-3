from contextlib import redirect_stderr
from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import formset_factory

from .models import Commission, Job, JobApplication
from .forms import CommissionForm, JobForm, JobFormSet ,JobApplicationForm 

def commissions_list(request):    
    commissions = Commission.objects.all()
    job_applicants = JobApplication.objects.all()
    ctx = {
        "commissions": commissions,
        "job_applicants": job_applicants
           }
    return render(request, "commissions_list.html", ctx)


def commissions_detail(request, pk):
    commission = Commission.objects.get(pk=pk)
    ctx = {"commission": commission}
    return render(request, "commission_detail.html", ctx)


def commissions_create(request):
    commission = Commission.objects.all()
    ctx = {"commission": commission}
    return render(request, "commissions_create.html", ctx)


def commissions_update(request, pk):
    commission = Commission.objects.get(pk=pk)
    ctx = {"commission": commission}
    return render(request, "commission_update.html", ctx)

class CommissionsListView(ListView):
    model = Commission
    template_name = 'commissions_list.html'


class CommissionsDetailView(DetailView):
    model = Commission
    template_name = 'commissions_detail.html'

    def post(self, request, *args, **kwargs):
        application_id = request.POST.get('application_id')
        job = get_object_or_404(Job, pk=application_id) # https://stackoverflow.com/questions/17813919/django-error-matching-query-does-not-exist
        accepted_applicants = JobApplication.objects.filter(status='Accepted').count()
        if accepted_applicants < job.manpower_required + 1:
            JobApplication.objects.create(job=JobApplication, applicant=request.user.profile)
            JobApplication.jobapplication_set.create(applicant=request.user.profile, status='Accepted')
            return redirect('commissions:commission', pk=self.kwargs['pk'])
        else:
            pass
    # # form_class1 = CommissionForm()
    # form_class = JobForm()


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     if self.request.POST:
    #         context['form'] = self.form_class(self.request.POST)
    #     else:
    #         context['form'] = self.form_class()
    #     return context

    # def form_valid(self, form):
    #     form.instance.author = self.request.user.profile
    #     context = self.get_context_data()
    #     job_formset = context['job_formset']
    #     if job_formset.is_valid():
    #         self.object = form.save()
    #         job_formset.instance = self.object
    #         job_formset.save()
    #         return super().form_valid(form)
    #     else:
    #         return self.render_to_response(self.get_context_data(form=form))


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = CommissionForm()
    #     context['commission'] = Commission.objects.all()
    #     context['job'] = Job.objects.all()
    #     return context
    

    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     form = CommissionForm(request.POST)
    #     if 'create_commission' in request.POST:


    #     '''
    #     if form.is_valid():
    #         commission = form.save(commit=False)
    #         commission.title = self.object
    #         commission.author = self.request.user.profile
    #         commission.save()
    #         return self.get(request, *args, **kwargs)
    #     else:
    #         self.object_list = self.get_queryset()
    #         context = self.get_context_data(**kwargs)
    #         context['form'] = form
    #         return self.render_to_response(context)
    #     '''


class CommissionsCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    template_name = 'commissions_create.html'
    form_class = CommissionForm

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


class CommissionsJobCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    template_name = 'commissions_create.html'
    fields = ['title', 'description', 'status', 'people_required']


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
       

class CommissionsUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Commission
    template_name = 'commissions_update.html'
    form_class = CommissionForm

    def test_func(self):
        obj = self.request.user.profile
        return obj.user == self.request.user