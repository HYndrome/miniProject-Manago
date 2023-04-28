from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm


# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'restaurants/index.html', context)


@login_required
def detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment_form = CommentForm()
    comments = post.comment_set.all()
    if request.method == 'POST':
        answer = request.POST['answer']
        if answer == post.option1 and request.user not in post.select1_contents.all():
            post.option1_count += 1
            post.selected_option = post.option1
            post.select1_contents.add(request.user)
            post.select2_contents.remove(request.user)
        elif answer == post.option2 and request.user not in post.select2_contents.all():
            post.option2_count += 1
            post.selected_option = post.option2
            post.select2_contents.add(request.user)
            post.select1_contents.remove(request.user)
        post.save()

    context = {'post': post,
               'comment_form':comment_form,
               'comments': comments,
               }
    return render(request, 'restaurants/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        option1 = request.POST['option1']
        option2 = request.POST['option2']
        user = request.user
        post = Post.objects.create(title=title, option1=option1, option2=option2, user=user)
        return redirect('posts:detail', post_pk=post.pk)
    return render(request, 'restaurants/create.html')


@login_required
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user == post.user:
        post.delete()
    return redirect('restaurants:index')


@login_required
def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user == post.user:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('restaurants:detail', post.pk)
        else:
            form = PostForm(instance=post)
    else:
        return redirect('restaurants:index')
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'restaurants/update.html', context)


@login_required
def comment_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
        return redirect('restaurants:detail', post.pk)
    context = {
        'post': post,
        'comment_form': comment_form,
    }
    return render(request, 'restaurants/detail.html', context)


@login_required
def comment_delete(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    if request.user == comment.user:
        comment.delete()
    return redirect('restaurants:detail', post_pk)


def answer(request, post_pk, answer):
    post = get_object_or_404(Post, pk=post_pk)
    if answer == '1':
        post.select1_contents.add(request.user)
    elif answer == '2':
        post.select2_contents.add(request.user)
    else:
        pass
    return redirect('restaurants:detail', pk=post_pk)