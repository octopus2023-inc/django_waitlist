# waitlist/forms.py

from django import forms
from .models import WaitlistEntry

class WaitlistForm(forms.ModelForm):
    class Meta:
        model = WaitlistEntry
        fields = ['email']
