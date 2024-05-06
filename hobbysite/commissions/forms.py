from django import forms

from .models import Commission, JobApplication


class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        exclude = ["author"]


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        exclude = ["author"]