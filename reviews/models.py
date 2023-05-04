from django.db import models
from django.conf import settings
from restaurants.models import Restaurant
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail
import os


class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    rate = models.IntegerField(default=3)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kargs):
        if self.reviewphoto_set:
            for review_photo in self.reviewphoto_set.all():
                os.remove(os.path.join(settings.MEDIA_ROOT, review_photo.image_review.path))
        super(Review, self).delete(*args, **kargs)

class ReviewPhoto(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    def image_path(instance, filename):
        return f'review_images/{instance.review.user.username}/{filename}'
    image_review = models.ImageField(upload_to=image_path)
    image_thumbnail = ImageSpecField(source='image_review',
                                      processors=[Thumbnail(200, 200)],
                                      format='JPEG',
                                      options={'quality': 100})
    

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
