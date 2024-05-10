from django.urls import path
from .views import CommissionsDetailView, CommissionsListView, CommissionsJobCreateView, CommissionsUpdateView

urlpatterns = [
    path('commissions/list', CommissionsListView.as_view(), name='commissions'),
    path('commissions/detail/<int:pk>', CommissionsDetailView.as_view(), name='commissions_detail'),
    path('commissions/add', CommissionsJobCreateView.as_view(), name='commissions_create'),
    path('commissions/<int:pk>/edit', CommissionsUpdateView.as_view(), name='commissions_update'),
]

app_name = 'commissions'