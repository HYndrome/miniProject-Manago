from django.shortcuts import render, redirect
from .models import Restaurant, Menu
from reviews.models import Review, ReviewPhoto
from reviews.forms import Review
from .forms import RestaurantForm, MenuForm
from reviews.forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Avg

# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()
    # Restaurant 평균 평점 갱신
    for restaurant in restaurants:
        reviews_averagerate = Review.objects.filter(restaurant_id=restaurant.pk).aggregate(Avg('rate'))['rate__avg']
        rt = Restaurant.objects.get(pk=restaurant.pk)
        rt.rate = reviews_averagerate
        rt.save()
    # Restaurant thumbnail 갱신
    flag = False
    for restaurant in restaurants:
        for review in restaurant.review_set.all():
            flag = False
            if flag == True:
                    break
            for reviewphoto in review.reviewphoto_set.all():
                if reviewphoto.image_review:
                    print(reviewphoto.image_review)
                    restaurant.image_first = reviewphoto.image_review
                    restaurant.save()
                    flag = True
                    break

    rankings = restaurants.order_by('-rate')[:8]
    eatdeals = Restaurant.objects.filter(eatdeal=True).order_by('-rate')[:8]
                    
    context = {
        'restaurants': restaurants,
        'eatdeals': eatdeals,
        'rankings': rankings,
    }
    return render(request, 'restaurants/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        restaurant_form = RestaurantForm(request.POST)
        if restaurant_form.is_valid():
            restaurant = restaurant_form.save(commit=False)
            restaurant.user = request.user
            restaurant.save()
            return redirect('restaurants:detail', restaurant.pk)
    else:
        restaurant_form = RestaurantForm()
    context = {
        'restaurant_form': restaurant_form,
    }
    return render(request, 'restaurants/create.html', context)

def detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    menus = restaurant.menu_set.all()
    reviews = Review.objects.filter(restaurant_id=restaurant_id)
    # 리뷰 평균 
    reviews_averagerate = Review.objects.filter(restaurant_id=restaurant_id).aggregate(Avg('rate'))['rate__avg']
    menu_form = MenuForm()
    review_form = ReviewForm()
    context = {
        'restaurant': restaurant,
        'menus': menus,
        'reviews': reviews,
        'menu_form': menu_form,
        'review_form': review_form,
        'reviews_averagerate': reviews_averagerate,
    }
    return render(request, 'restaurants/detail.html', context)

@login_required
def delete(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    if request.user == restaurant.user:
        restaurant.delete()
    return redirect('restaurants:index')

@login_required
def menu(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    menu_form = MenuForm(request.POST)
    if menu_form.is_valid():
        menu = menu_form.save(commit=False)
        menu.restaurant = restaurant
        menu.user = request.user
        menu.save()
        return redirect('restaurants:detail', restaurant.pk)
    context = {
        'restaurant': restaurant,
        'menu_form': menu_form,
    }
    return render(request, 'restaurants/detail.html', context)

@login_required
def menu_delete(request, restaurant_id, menu_id):
    menu = Menu.objects.get(pk=menu_id)
    if request.user == menu.user:
        menu.delete()
    return redirect('restaurants:detail', restaurant_id)

@login_required
def wish(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    if request.user in restaurant.wish_users.all():
        restaurant.wish_users.remove(request.user)
        is_wished = False
    else:
        restaurant.wish_users.add(request.user)
        is_wished = True
    context = {
        'is_wished': is_wished
    }
    return JsonResponse(context)

def category(request, restaurant_category):
    category_restaurants = Restaurant.objects.filter(category=restaurant_category).order_by('-rate')
    reviews = Review.objects.all()
    for restaurant in category_restaurants:
        reviews = Review.objects.filter(restaurant_id=restaurant.pk)
        restaurant.first_review = Review.objects.filter(restaurant_id=restaurant.pk).order_by('-created_at').first()
        restaurant.save()
    context = {
            'restaurant_category': restaurant_category,
            'category_restaurants': category_restaurants,
            'reviews': reviews,
        }
    return render(request, 'restaurants/category.html', context)

def eatdeal(request):
    restaurants = Restaurant.objects.filter(eatdeal=True).order_by('-rate')
    reviews = Review.objects.all()
    for restaurant in restaurants:
        reviews = Review.objects.filter(restaurant_id=restaurant.pk)
        restaurant.first_review = Review.objects.filter(restaurant_id=restaurant.pk).order_by('-created_at').first()
        restaurant.save()
    context = {
        'restaurants': restaurants,
        'reviews': reviews,
    }
    return render(request, 'restaurants/eatdeal.html', context)

def region(request, restaurant_region):
    region_restaurants = Restaurant.objects.filter(region=restaurant_region).order_by('-rate')
    reviews = Review.objects.all()
    for restaurant in region_restaurants:
        reviews = Review.objects.filter(restaurant_id=restaurant.pk)
        restaurant.first_review = Review.objects.filter(restaurant_id=restaurant.pk).order_by('-created_at').first()
        restaurant.save()
    context = {
        'restaurant_region': restaurant_region,
        'region_restaurants': region_restaurants,
        'reviews': reviews,
    }
    return render(request, 'restaurants/region.html', context)

