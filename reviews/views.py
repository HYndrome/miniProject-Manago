from django.shortcuts import render, redirect
from restaurants.models import Restaurant
from .models import Review, Comment
from .forms import ReviewForm

def create(request, restaurant_id):
    if request.method == 'POST':
        restaurant = Restaurant.objects.get(pk=restaurant_id)
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.restaurant = restaurant
            review.save()
            return redirect('reviews:detail', restaurant_id=restaurant_id, review_id=review.id)
    else:
        form = ReviewForm
    context = {
        'form': form,
        'restaurant_id': restaurant_id,
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
    review = Review.objects.get(pk=review_id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews:detail', restaurant_id=restaurant_id, review_id=review.id)
    else:
        form = ReviewForm(instance=review)
    context = {
        'form': form,
        'review': review,
        'restaurant_id': restaurant_id,
        'review_id': review_id,
    }
    return render(request, 'reviews/update.html', context)
    
    
def likes(request, restaurant_id, review_id):
    # POST
    return render(request, 'reviews/likes.html',)


def comment_create(request, restaurant_id, review_id):
    # POST
    return render(request, 'reviews/comment_create.html')


def comment_delete(request, restaurant_id, review_id, comment_id):
    # POST
    return render(request, 'reviews/comment_delete.html')
