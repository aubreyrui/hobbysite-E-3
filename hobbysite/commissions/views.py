from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Commission

def commissions_list(request):
    commissions = Commission.objects.all()
    ctx = {"commissions": commissions}
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


class CommissionsCreateView(CreateView):
    model = Commission
    template_name = 'commissions_create.html'


class CommissionsUpdateView(UpdateView):
    model = Commission
    template_name = 'commissions_update.html'