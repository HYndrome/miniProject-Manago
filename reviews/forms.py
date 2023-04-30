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



# from django.forms.widgets import Input

# class ImageRadioInput(Input):
#     input_type = 'radio'

#     def render(self, name, value, attrs=None, renderer=None):
#         if 'enabled_image' in self.attrs:
#             enabled_image = self.attrs.pop('enabled_image')
#         else:
#             enabled_image = ''
#         if 'disabled_image' in self.attrs:
#             disabled_image = self.attrs.pop('disabled_image')
#         else:
#             disabled_image = ''
#         if value == self.attrs['value']:
#             final_attrs = dict(attrs, checked='', class_='enabled')
#         else:
#             final_attrs = dict(attrs, class_='disabled')
#         rendered = super().render(name, value, final_attrs, renderer)
#         return f'<label><img src="{enabled_image}" class="enabled"><img src="{disabled_image}" class="disabled">{rendered}</label>'
    

# class ReviewForm(forms.ModelForm):
#     rate = forms.ChoiceField(
#         choices=[
#             ('option1', 'Option 1'), 
#             ('option2', 'Option 2')
#         ], 
#         widget=ImageRadioInput(
#             attrs={
#                 'enabled_image': '% static \'reviews/good_face_act.png\' %', 
#                 'disabled_image': '% static \'reviews/good_face.png\' %'
#             }
#         )
#     )
#     class Meta:
#         model = Review
#         fields = ('rate', 'content',)




class ReviewForm(forms.ModelForm):
    # rate = forms.IntegerField(
    #     widget = forms.RadioSelect(
    #         choices = (
    #             (5, '맛있다'),
    #             (3, '괜찮다'),
    #             (1, '별로'),
    #         ),
    #         attrs = {
    #             # 'class': 'form-check-input',
    #             # 'id': 'rate',
    #             # 'name': 'rate',
    #         },
    #     ),
    #     required = True
    # )

    content = forms.CharField(
        widget = forms.Textarea(
            attrs = {
                'class': 'form-control',
                'id': 'content',
                'name': 'content',
                'rows': 3,
                'cols': 50,
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
    class Meta:
        model = Comment
        fields = ('content',)