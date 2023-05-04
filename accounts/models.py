from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from django.db import models
from imagekit.processors import Thumbnail




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
