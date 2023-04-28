from django.shortcuts import render
from restaurants.models import Restaurant
from .models import Review, Comment
from .forms import ReviewForm

def create(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    review_form = ReviewForm(request.POST)
    pass
def detail(request, restaurant_id, review_id):
    review = Review.objects.get(pk=review_id)
    context = {
        'review': review
        }
    return render(request, 'reviews/detail.html', context)
def delete(request, restaurant_id, review_id):
    pass
def update(request, restaurant_id, review_id):
    pass
def likes(request, restaurant_id, review_id):
    pass
def comment_create(request, restaurant_id, review_id):
    pass
def comment_delete(request, restaurant_id, review_id, comment_id):
    pass

