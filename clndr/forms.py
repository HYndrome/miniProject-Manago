from django import forms
from .models import Meet

class MeetForm(forms.ModelForm):
    class Meta:
        model = Meet
        fields = ('name', 'content')