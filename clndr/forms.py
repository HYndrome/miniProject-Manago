from django import forms
from .models import Meet, Comment

class MeetForm(forms.ModelForm):
    name = forms.CharField(
        label = False,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '모임 이름을 입력하세요',
                'maxlength': 50,
            }
        ),
    )
    content = forms.CharField(
        label = False,
        widget = forms.Textarea(
            attrs = {
                'class': 'form-control',
                'placeholder': '모임 내용을 입력하세요',
                'rows': 5,
            }
        ),
    )
    class Meta:
        model = Meet
        fields = ('name', 'content')

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label = False,
        widget = forms.Textarea(
            attrs = {
                'class': 'form-control',
                'placeholder': '댓글 내용을 입력해주세요.',
                'rows': 3,
            }
        )
    )
    class Meta:
        model = Comment
        fields = ('content',)