from django.shortcuts import render, redirect
from restaurants.models import Restaurant
from .models import Review, Comment, ReviewPhoto
from .forms import ReviewForm, CommentForm
from django.contrib.auth.decorators import login_required


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
            print(request.FILES.getlist('image_review'))
            for img in request.FILES.getlist('image_review'):
                print(img)
                # Photo 객체를 하나 생성한다.
                photo = ReviewPhoto()
                # 외래키로 현재 생성한 Post의 기본키를 참조한다.
                photo.review = review
                # imgs로부터 가져온 이미지 파일 하나를 저장한다.
                photo.image_review = img
                # 데이터베이스에 저장
                photo.save()
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
    if request.user != review.user:
        return redirect('reviews:detail', restaurant_id=restaurant_id, review_id=review_id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews:detail', restaurant_id=restaurant_id, review_id=review_id)
    else:
        form = ReviewForm(instance=review, user=request.user)
    context = {
        'form': form,
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
    else:
        review.like_users.add(request.user)
    return redirect('reviews:detail', restaurant_id=restaurant_id, review_id=review_id)


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
def comment_delete(request, restaurant_id, review_id, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('reviews:detail', restaurant_id=restaurant_id, review_id=review_id)
