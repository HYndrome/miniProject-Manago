from django.shortcuts import render, redirect
from restaurants.models import Restaurant
from .models import Review, Comment, ReviewPhoto
from .forms import ReviewForm, CommentForm, ReviewPhotoForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

@login_required
def create(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.restaurant = restaurant
            review.rate = int(request.POST.get('rate'))
            review.save()
            for img in request.FILES.getlist('image_review'):
                photo = ReviewPhoto()
                photo.review = review
                photo.image_review = img
                photo.save()
            return redirect('reviews:detail', restaurant_id=restaurant_id, review_id=review.id)
    else:
        form = ReviewForm(user=request.user)
        image_form = ReviewPhotoForm()
    context = {
        'form': form,
        'image_form': image_form,
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
    
    
@login_required
def delete(request, restaurant_id, review_id):
    review = Review.objects.get(pk=review_id)
    if request.user != review.user:
        return redirect('reviews:detail', restaurant_id=restaurant_id, review_id=review_id)
    review.delete()
    return redirect('restaurants:detail', restaurant_id=restaurant_id)
    
    
@login_required
def update(request, restaurant_id, review_id):
    review = Review.objects.get(pk=review_id)
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    image = ReviewPhoto.objects.filter(review_id=review.pk)
    images = review.reviewphoto_set.all()
    if request.user != review.user:
        return redirect('reviews:detail', restaurant_id=restaurant_id, review_id=review_id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES, instance=review)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.rate = int(request.POST.get('rate'))
            review.save()
            # review.reviewphoto_set.all().delete()
            for img in request.FILES.getlist('image_review'):
                photo = ReviewPhoto()
                photo.review = review
                photo.image_review = img
                photo.save()
            images_to_delete = request.POST.getlist('delete_images')
            for image_id in images_to_delete:
                # image = get_object_or_404(Image, id=image_id)
                image = ReviewPhoto.objects.get(id=image_id)
                image.delete()
            return redirect('reviews:detail', restaurant_id=restaurant_id, review_id=review_id)
    else:
        form = ReviewForm(instance=review, user=request.user)
        image_form = ReviewPhotoForm()
    context = {
        'form': form,
        'image_form': image_form,
        'images': images,
        'review': review,
        'restaurant': restaurant,
        'restaurant_id': restaurant_id,
        'review_id': review_id,
    }
    return render(request, 'reviews/update.html', context)
    
    
@login_required
def likes(request, restaurant_id, review_id):
    review = Review.objects.get(pk=review_id)
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
        is_liked = False
    else:
        review.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
        'review_like_count': review.like_users.count(),
    }
    return JsonResponse(context)


@login_required
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


@login_required
def comment_update(request, restaurant_id, review_id, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        if request.method == 'POST':
            jsonObject = json.loads(request.body)
            comment.content = jsonObject['content']
            comment.save()

    context = {
        'content': comment.content,
    }
    return JsonResponse(context)


@login_required
def comment_delete(request, restaurant_id, review_id, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('reviews:detail', restaurant_id=restaurant_id, review_id=review_id)