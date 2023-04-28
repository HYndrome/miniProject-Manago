from django import forms
from .models import Restaurant, Menu

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('name', 'address', 'phone', 'category', 'pricerange', 'parking', 'time_open', 'time_close', 'time_break_start', 'time_break_end', 'time_lastorder', 'eatdeal')

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('name', 'price')