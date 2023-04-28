from django.shortcuts import render, redirect
from .models import Restaurant, Menu
from .forms import RestaurantForm, MenuForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'restaurants/index.html')

@login_required
def create(request):
    if request.method == 'POST':
        restaurant_form = RestaurantForm(request.POST)
        menu_form = MenuForm(request.POST)
        if restaurant_form.is_valid():
            if menu_form.is_valid():
                restaurant = restaurant_form.save(commit=False)
                restaurant.user = request.user
                restaurant.save()
                menu = menu_form.save(commit=False)
                menu.restaurant = restaurant
                menu.save()
                return redirect('restaurants:detail', restaurant.pk)
    else:
        restaurant_form = RestaurantForm()
        menu_form = MenuForm()
    context = {
        'restaurant_form': restaurant_form,
        'menu_form': menu_form,
    }
    return render('restaurants/index.html', context)

def detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    menu = Menu.objects.get(restaurant=restaurant)
    # review_form = ReviewForm()
    context = {
        'restaurant': restaurant,
        'menu': menu,
        # 'review_form': review_form
    }
    return render(request, 'restaurants/detail.html', context)

# @login_required
# def wish(request, restaurant_id):
#     restaurant = Restaurant.objects.get(pk=restaurant_id)
#     if request.user in restaurant.wish_users
#     return

def category(request, restaurant_category):
    return

def eatdeatl(request):
    return

def region(request, restaurant_address):
    return