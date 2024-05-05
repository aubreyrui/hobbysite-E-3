from django.views.generic.edit import UpdateView
from .forms import ProfileForm
from .models import Profile
from django.urls import reverse_lazy

class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = "user_management_update.html"
    form_class = ProfileForm

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.display_name = form.cleaned_data['display_name'] #manually accessing the values
        profile.email_address = form.cleaned_data['email_address']
        profile.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("user_management:profile_update")    
    