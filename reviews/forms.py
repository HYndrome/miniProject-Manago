from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    content = forms.CharField(
        label = False,
        widget = forms.Textarea(
            attrs = {
                'class': 'form-control',
                'id': 'content',
                'rows': 6,
            }
        )
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['content'].widget.attrs.update({'placeholder': f'{user.username}님, 주문하신 메뉴는 어떠셨나요? 식당의 분위기와 서비스도 궁금해요!'})

    class Meta:
        model = Review
        fields = ('content',)


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