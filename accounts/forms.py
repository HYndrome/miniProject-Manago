from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='ID',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )

    email = forms.CharField(
        label='e-mail',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'type': 'email',
            },
        ),
    )

    name = forms.CharField(
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'type': 'password',
            },
        ),
    )

    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'type': 'password',
            },
        ),
    )

    region = forms.CharField(
        label = '지역',
        widget=forms.Select(
            attrs={
                'class': 'form-select',
            
            },
            choices= [
                ("서울", "서울특별시"),
                ("경기도", "경기도"),
                ("인천", "인천광역시"),
                ("강원도", "강원도"),
                ("전라북도", "전라북도"),
                ("전라남도", "전라남도"),
                ("경상북도", "경상북도"),
                ("경상남도", "경상남도"),
            ]
        )
    )

    image = forms.ImageField(
        label = '이미지',
        required = False,
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields =(
            'username',
            'email',
            'name',
            'password1',
            'password2',
            'region',
            'image',
            )


class CustomUserChangeForm(UserChangeForm):
    email = forms.CharField(
        label='e-mail',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'type': 'email',
            },
        ),
    )

    last_name = forms.CharField(
        label='성',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    first_name = forms.CharField(
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    image = forms.ImageField(
        label = '이미지',
        required=False,
    )

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = (
            'email',
            'last_name',
            'first_name',
    )
        

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='ID',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'type': 'password',
            },
        ),
    )

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )
        

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="기존 비밀번호",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    new_password1 = forms.CharField(
        label="새 비밀번호",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    new_password2 = forms.CharField(
        label="새 비밀번호 확인",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('old_password', 'new_password1', 'new_password2')