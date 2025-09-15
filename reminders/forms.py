from django import forms
from .models import Reminder


class CreateReminder(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'description', 'date']