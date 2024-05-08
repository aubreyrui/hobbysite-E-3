from contextlib import redirect_stderr
from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import formset_factory
from django.http import HttpResponseBadRequest
from django.db.models import Sum

from .models import Commission, Job, JobApplication
from .forms import CommissionForm, JobFormSet ,JobApplicationForm 

def commissions_list(request):    
    commissions = Commission.objects.all()
    job_applicants = JobApplication.objects.all()
    ctx = {
        "commissions": commissions,
        "job_applicants": job_applicants
           }
    return render(request, "commissions_list.html", ctx)


def commissions_detail(self, request, pk):
    commission = Commission.objects.get(pk=pk)
    job_applications = JobApplication.objects.all()
    ctx = {
        "commission": commission,
        "job_application": job_applications
           }
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
    form_class = JobApplicationForm

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        context = super(CommissionsDetailView, self).get_context_data(**kwargs)
        total_manpower_required = Job.objects.aggregate(total_manpower=Sum('manpower_required'))['total_manpower'] or 0
        total_signees = JobApplication.objects.filter(status='Accepted').count()
        open_manpower = max(total_manpower_required - total_signees, 0)
        context['total_manpower_required'] = total_manpower_required
        context['total_signees'] = total_signees
        context['open_manpower'] = open_manpower
        return context
    

    def post(self, request, *args, **kwargs):
        self.object = self.get_object() # gets the Commission object
        job_application_form = JobApplicationForm(request.POST)
        if job_application_form.is_valid():
            job_application = job_application_form.save(commit=False) # create commission object but does not save
            job_application.commission = self.object
            print(job_application.commission)
            job_application.applicant = self.request.user.profile
            print(job_application.job)
            job_application.save()
            return redirect('commissions:commissions')
        else:
            return self.render_to_response(self.get_context_data(form=job_application_form))
        

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
       

class CommissionsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Commission
    template_name = 'commissions_update.html'
    form_class = CommissionForm

    def test_func(self):
        obj = self.request.user.profile
        return obj.user == self.request.user
    
    # if model.job.status == 'Full':
