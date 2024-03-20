from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Commission

def commissions_list(request):
    commissions = Commission.objects.all()
    ctx = {"commissions": commissions}
    return render(request, "commissions_list.html", ctx)


def commissions_detail(request, pk):
    commission = Commission.objects.get(pk=pk)
    ctx = {"commission": commission}
    return render(request, "commission_detail.html", ctx)


class CommissionsListView(ListView):
    model = Commission
    template_name = 'commissions_list.html'


class CommissionsDetailView(DetailView):
    model = Commission
    template_name = 'commissions_detail.html'