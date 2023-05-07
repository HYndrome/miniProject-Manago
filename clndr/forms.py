from django import forms
from .models import Meet

class MeetForm(forms.ModelForm):
    name = forms.CharField(
        label = '모임 이름',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '모임 이름을 입력하세요',
                'maxlength': 50,
            }
        ),
    )
    content = forms.CharField(
        label = '모임 내용',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '모임 내용을 입력하세요',
                'maxlength': 200,
            }
        ),
    )
    class Meta:
        model = Meet
        fields = ('name', 'content')