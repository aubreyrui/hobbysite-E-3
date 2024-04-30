from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import UpdateView
from .forms import ProfileForm
from .models import Profile
from django.urls import reverse_lazy

class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = "user_management_update.html"
    form_class = ProfileForm

    def get_object(self, queryset=None):#https://stackoverflow.com/questions/6181041/updating-user-model-in-django-with-class-based-updateview
        # This assumes that each user has a one-to-one relationship with a Profile
        return self.request.user

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("user_management:profile_update")    