from django.views.generic.edit import UpdateView, CreateView
from .forms import UpdateProfileForm, CreateProfileForm
from .models import Profile
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import redirect_to_login

class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = "user_management_update.html"
    form_class = UpdateProfileForm

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.display_name = form.cleaned_data['display_name'] #manually accessing the values
        profile.email_address = form.cleaned_data['email_address']
        profile.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("landing_page")
    
class ProfileCreateView(CreateView):
    model = Profile
    template_name = "user_management_create.html"
    form_class = CreateProfileForm

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        form = ctx["form"]
        ctx["form"] = form
        return ctx
    
    def get_success_url(self):
        return reverse_lazy("landing_page")