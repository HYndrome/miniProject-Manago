from django import forms
from .models import Review, Comment

# from itertools import chain
# from django.utils.safestring import mark_safe
# from django.forms.widgets import RadioSelect

# class ImageRadioSelect(RadioSelect):
#     def render(self, name, value, attrs=None, choices=()):
#         output = []
#         for i, (option_value, option_label) in enumerate(chain(self.choices, choices)):
#             output.append('<label>')
#             output.append('<input type="radio" name="%s" value="%s" %s>' % (name, option_value, 'checked' if str(option_value) == str(value) else ''))
#             output.append('<img src="%s" alt="%s">' % (option_label, option_value))
#             output.append('</label>')
#         return mark_safe('\n'.join(output))





# from django import forms

# class MyForm(forms.Form):
#     my_field = forms.ChoiceField(
#         choices=[
#             ('value1', 'image1.jpg'), 
#             ('value2', 'image2.jpg')
#         ], 
#         widget=ImageRadioSelect)








class ReviewForm(forms.ModelForm):
    rate = forms.IntegerField(
        widget = forms.RadioSelect(
            choices = (
                (5, '맛있다'),
                (3, '괜찮다'),
                (1, '별로'),
            ),
            attrs = {
                # 'class': 'form-check-input',
                # 'id': 'rate',
                # 'name': 'rate',
            },
        ),
        required = True
    )

    class Meta:
        model = Review
        fields = ('rate', 'content',)









class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)