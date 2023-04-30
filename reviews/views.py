from django.shortcuts import render, redirect
from restaurants.models import Restaurant
from .models import Review, Comment
from .forms import ReviewForm, CommentForm


def create(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
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
        form = ReviewForm(user=request.user)
    context = {
        'form': form,
        'restaurant': restaurant,
        'restaurant_id': restaurant_id,
    }
    return render(request, 'reviews/create.html', context)
    
    
def detail(request, restaurant_id, review_id):
    review = Review.objects.get(pk=review_id)
    comment_form = CommentForm()
    comments = Comment.objects.filter(review_id=review_id)
    context = {
        'review': review,
        'comment_form': comment_form,
        'restaurant_id': restaurant_id,
        'review_id': review_id,
        'comments': comments,
    }
    return render(request, 'reviews/detail.html', context)
    
    
def delete(request, restaurant_id, review_id):
    review = Review.objects.get(pk=review_id)
    review.delete()
    return redirect('restaurants:detail', restaurant_id=restaurant_id)
    
    
def update(request, restaurant_id, review_id):
    review = Review.objects.get(pk=review_id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews:detail', restaurant_id=restaurant_id, review_id=review_id)
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
    review = Review.objects.get(pk=review_id)
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    return redirect('reviews:detail', restaurant_id=restaurant_id, review_id=review_id)

def comment_create(request, restaurant_id, review_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    review = Review.objects.get(pk=review_id)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.review = review
        comment.restaurant = restaurant
        comment.save()
        return redirect('reviews:detail', restaurant_id=restaurant_id, review_id=review_id)
    context = {
        'comment_form': comment_form,
    }
    return redirect('reviews:detail', restaurant_id=restaurant_id, review_id=review_id, context=context)


def comment_delete(request, restaurant_id, review_id, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('reviews:detail', restaurant_id=restaurant_id, review_id=review_id)
