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
            ("서울", "서울"),
            ("부산", "부산"),
            ("대구", "대구"),
            ("인천", "인천"),
            ("광주", "광주"),
            ("대전", "대전"),
            ("울산", "울산"),
            ("세종", "세종"),
            ("경기도", "경기도"),
            ("강원도", "강원도"),
            ("충청북도", "충청북도"),
            ("충청남도", "충청남도"),
            ("전라북도", "전라북도"),
            ("전라남도", "전라남도"),
            ("경상북도", "경상북도"),
            ("경상남도", "경상남도"),
            ("제주도", "제주도")
        ]
        ),
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
        label = '음식종류',
        widget=forms.Select(
            attrs={
                'class': 'form-select',
            },
        choices= [
            ("족발,보쌈", "족발,보쌈"),
            ("찜,탕,찌개", "찜,탕,찌개"),
            ("돈까스,회,일식", "돈까스,회,일식"),
            ("피자", "피자"),
            ("고기,구이", "고기,구이"),
            ("야식", "야식"),
            ("양식", "양식"),
            ("치킨", "치킨"),
            ("중식", "중식"),
            ("아시안", "아시안"),
            ("백반,죽,국수", "백반,죽,국수"),
            ("도시락", "도시락"),
            ("분식", "분식"),
            ("카페,디저트", "카페,디저트"),
            ("패스트푸드", "패스트푸드"),
            ("기타", "기타"),
        ]
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
                'maxLength': 50,
            }
        )
    )
    time_lastorder = forms.CharField(
        label = '마지막 주문',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '마지막 주문 시간을 입력하세요',
                'maxLength': 50,
            }
        )
    )
    # eatdeal = forms.ChoiceField(
    #     label = '잇딜',
    #     widget = forms.Select(
    #         attrs = {
    #             'class': 'form-select',
    #             'placeholder': '잇딜 진행 중 여부를 입력하세요'
    #         },
    #     choices = [
    #         (True, "잇딜 진행 중"),
    #         (False, "잇딜 진행 중 아님")
    #     ]
    #     )
    # )
    eatdeal = forms.ChoiceField(
        label = '잇딜',
        widget = forms.Select(
            attrs = {
                'class': 'form-select',
                'placeholder': '잇딜 진행 중 여부를 입력하세요'
            },
        ),
        choices = [
            (True, "잇딜 진행 중"),
            (False, "잇딜 진행 중 아님")
        ],
    )
    class Meta:
        model = Restaurant
        fields = ('name', 'address', 'phone', 'category', 'region', 'pricerange', 'parking', 'business_hours', 'time_lastorder', 'eatdeal')

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