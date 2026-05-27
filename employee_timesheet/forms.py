from django import forms
from .models import Timesheet

class TimesheetForm(forms.ModelForm):
    class Meta:
        model = Timesheet
        fields = ['date', 'task', 'hours', 'comments']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
