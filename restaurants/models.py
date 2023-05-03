from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail

category_CHOICES = [
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
region_CHOICES = [
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
class Restaurant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    wish_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wish_restaurants')
    name = models.CharField(max_length=50)
    views = models.PositiveIntegerField(default=0)
    region = models.CharField(max_length=20, choices=region_CHOICES)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, null=True, blank=True)
    category = models.CharField(max_length=20, choices=category_CHOICES)
    pricerange = models.CharField(max_length=50, null=True, blank=True)
    parking = models.CharField(max_length=50, null=True, blank=True)
    business_hours = models.CharField(max_length=50, null=True, blank=True)
    time_lastorder = models.CharField(max_length=50, null=True, blank=True)
    eatdeal = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rate = models.IntegerField(null=True, blank=True)
    image_first = models.ImageField(null=True, blank=True)
    image_thumbnail = ImageSpecField(source='image_first',
                                      processors=[Thumbnail(200, 200)],
                                      format='JPEG',
                                      options={'quality': 100})

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.CharField(max_length=50, null=True, blank=True)