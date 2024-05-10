from django.urls import path
from .views import ProfileUpdateView, ProfileCreateView

urlpatterns = [
    path('profile/update', ProfileUpdateView.as_view(), name = 'profile_update'),
    path('profile/sign_up', ProfileCreateView.as_view(), name = 'profile_create')    
]
app_name = 'user_management'