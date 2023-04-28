from django.db import models
from django.conf import settings

class Restaurant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    wish_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wish_restaurants')
    name = models.CharField(max_length=50)
    views = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    pricerange = models.CharField(max_length=50, null=True, blank=True)
    parking = models.CharField(max_length=50, null=True, blank=True)
    time_open = models.TimeField(null=True, blank=True)
    time_close = models.TimeField(null=True, blank=True)
    time_break_start = models.TimeField(null=True, blank=True)
    time_break_end = models.TimeField(null=True, blank=True)
    time_lastorder = models.TimeField(null=True, blank=True)
    eatdeal = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.CharField(max_length=50, null=True, blank=True)