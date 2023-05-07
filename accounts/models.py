from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from django.db import models
from imagekit.processors import Thumbnail

CHOICES_REGION = [
    ("서울", "서울특별시"),
    ("경기도", "경기도"),
    ("인천", "인천광역시"),
    ("강원도", "강원도"),
    ("전라북도", "전라북도"),
    ("전라남도", "전라남도"),
    ("경상북도", "경상북도"),
    ("경상남도", "경상남도"),
]


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=10)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    # image = models.ImageField(blank=True, upload_to='')
    image = ProcessedImageField(
        null=True,
        blank=True,
        processors=[Thumbnail(200,200)],
        format= 'JPEG',
        options= {'quality':90},
        upload_to = '',
    )
    region = models.CharField(max_length=10, choices=CHOICES_REGION)
