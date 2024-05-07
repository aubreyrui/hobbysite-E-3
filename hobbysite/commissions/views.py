from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from .models import Commission, JobApplication
from .forms import CommissionForm, JobApplicationForm 

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


class CommissionsCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    template_name = 'commissions_create.html'
    form_class = CommissionForm

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


class JobCreateView(LoginRequiredMixin, CreateView):
    model = JobApplication
    template_name = 'commissions_create.html'
    form_class = JobApplicationForm

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


class CommissionsUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Commission
    template_name = 'commissions_update.html'
    form_class = CommissionForm

    def test_func(self):
        obj = self.request.user.profile
        return obj.user == self.request.user