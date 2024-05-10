from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name', 'email_address']

class CreateProfileForm(UserCreationForm): 
    # https://www.javatpoint.com/django-usercreationform#:~:text=Django%20UserCreationForm%20is%20used%20for,contrib.
    model = Profile
    fields = '__all__'
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = Profile.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username 

    def displayname_clean(self):  
        display_name = self.cleaned_data['username'].lower()  
        new = Profile.objects.filter(display_name = display_name)  
        if new.count():  
            raise ValidationError("Display Name Already Exist")  
        return display_name  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = Profile.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  

        return password1  
    
