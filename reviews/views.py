from django.shortcuts import render
from restaurants.models import Restaurant
from .models import Review, Comment
from .forms import ReviewForm

def create(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    review_form = ReviewForm(request.POST)
    context = {

    }
    return render(request, 'reviews/create.html', context)
    
    
def detail(request, restaurant_id, review_id):
    review = Review.objects.get(pk=review_id)
    context = {
        'review': review
        }
    return render(request, 'reviews/detail.html', context)
    
    
def delete(request, restaurant_id, review_id):
    # POST
    return render(request, 'reviews/delete.html',)
    
    
def update(request, restaurant_id, review_id):
    return render(request, 'reviews/update.html',)
    
    
def likes(request, restaurant_id, review_id):
    # POST
    return render(request, 'reviews/likes.html',)


def comment_create(request, restaurant_id, review_id):
    # POST
    return render(request, 'reviews/comment_create.html')


def comment_delete(request, restaurant_id, review_id, comment_id):
    # POST
    return render(request, 'reviews/comment_delete.html')
