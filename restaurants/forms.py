from django import forms
from .models import Restaurant, Menu

class RestaurantForm(forms.ModelForm):
    name = forms.CharField(
        label = '식당 이름',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '식당 이름을 입력하세요',
                'maxlength': 50,
            }
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
    address = forms.CharField(
        label = '주소',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '주소를 입력하세요',
                'maxLength': 100,
            }
        ),
    )
    phone = forms.CharField(
        label = '전화번호',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '전화번호를 입력하세요',
                'maxLength': 50,
            }
        ),
    )
    category = forms.CharField(
        label = '음식 종류',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '음식 종류를 입력하세요',
                'maxLength': 50,
            }
        ),
    )
    pricerange = forms.CharField(
        label = '가격대',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '가격대를 입력하세요',
                'maxLength': 50,
            }
        ),
    )
    parking = forms.CharField(
        label = '주차 가능 여부',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '주차 가능 여부를 입력하세요',
                'maxLength': 50,
            }
        ),
    )
    business_hours = forms.CharField(
        label = '영업 시간',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '영업 시간을 입력하세요',
                'maxLength': 100,
            }
        )
    )
    time_lastorder = forms.TimeField(
        label = '마지막 주문',
        widget = forms.TimeInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '마지막 주문 시간을 입력하세요',
            }
        )
    )
    eatdeal = forms.BooleanField(
        label = '잇딜',
        widget = forms.Select(
            attrs = {
                'class': 'form-select',
                'placeholder': '잇딜 진행 중 여부를 입력하세요'
            },
            choices = [
                (True, "잇딜 진행 중"),
                (False, "잇딜 진행 중 아님")
            ]
        )
    )
    class Meta:
        model = Restaurant
        fields = ('name', 'address', 'phone', 'category', 'pricerange', 'parking', 'business_hours', 'time_lastorder', 'eatdeal')

class MenuForm(forms.ModelForm):
    name = forms.CharField(
        label = '메뉴 이름',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '메뉴 이름을 입력하세요',
                'maxlength': 50,
            }
        ),
    )
    price = forms.CharField(
        label = '가격',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '가격을 입력하세요',
                'maxLength': 50,
            }
        ),
    )
    class Meta:
        model = Menu
        fields = ('name', 'price')