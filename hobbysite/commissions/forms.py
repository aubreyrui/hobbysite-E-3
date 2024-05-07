from django import forms

from .models import Commission, Job, JobApplication


class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        exclude = ["author"]


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['role', 'manpower_required', 'status']


JobFormSet = forms.inlineformset_factory(
    Commission, Job, form=JobForm, extra=1, can_delete=False # https://docs.djangoproject.com/en/5.0/topics/forms/formsets/
)

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        exclude = ["author"]

