from django.urls import path
from .views import CommissionsDetailView, CommissionsListView

urlpatterns = [
    path('commissions/list', CommissionsListView.as_view(), name='commissions'),
    path('commissions/detail/<int:pk>', CommissionsDetailView.as_view(), name='commissions_detail'),
]

app_name = 'commissions'