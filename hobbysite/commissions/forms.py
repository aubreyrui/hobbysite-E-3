from django import forms

from .models import Commission


class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        exclude = ["author"]