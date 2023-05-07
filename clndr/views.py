from django.shortcuts import render, redirect
from .models import Meet, Comment
from .forms import MeetForm, CommentForm
import json, datetime
from datetime import timedelta, datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
from django.contrib.auth.decorators import login_required

# Create your views here.

def main(request):
    # Meet.objects.all().delete()

    meet_form = MeetForm()
    context = {
        'meet_form': meet_form,
    }
    return render(request, 'clndr/main.html', context)

@login_required
def meet(request):
    # Get the selected date data from the form
    selected_date = request.POST.get('selected-date')
    if selected_date is not None:
        selDate = json.loads(selected_date)
    meet_form = MeetForm(request.POST)
    if meet_form.is_valid():
        meet = meet_form.save(commit=False)
        meet.user = request.user
        meet.date = selDate
        meet.save()
        return redirect('clndr:main')
    
def detail(request, urlDate):
    meets = Meet.objects.filter(date=urlDate)
    context = {
        'meets': meets,
    }
    return render(request, 'clndr/detail.html', context)

@login_required
def attend(request, meet_id):
    meet = Meet.objects.get(pk=meet_id)
    if request.user in meet.attend_users.all():
        meet.attend_users.remove(request.user)
        is_attending = False
    else:
        meet.attend_users.add(request.user)
        is_attending = True
    context = {
        'is_attending': is_attending,
    }
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def meet_detail(request, meet_id):
    meet = Meet.objects.get(pk=meet_id)
    comment_form = CommentForm()
    comments = Comment.objects.filter(meet = meet)
    context = {
        'meet': meet,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'clndr/meet_detail.html', context)

@login_required
def delete(request, meet_id):
    meet = Meet.objects.get(pk=meet_id)
    meet.delete()
    return redirect('clndr:main')

@login_required
def comment(request, meet_id):
    meet = Meet.objects.get(pk=meet_id)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.meet = meet
        comment.user = request.user
        comment.save()
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    context = {
        'comment_form': comment_form,
    }
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'), context=context)

@login_required
def update(request, meet_id):
    meet = Meet.objects.get(pk=meet_id)
    if request.user == meet.user:
        if request.method == 'POST':
            meet_form = MeetForm(request.POST, instance=meet)
            if meet_form.is_valid():
                meet_form.save()
                return redirect('clndr:meet_detail', meet.pk)
        else:
            meet_form = MeetForm(instance=meet)
    else:
        return redirect('clndr:detail', meet.pk)
    context = {
        'meet': meet,
        'meet_form': meet_form,
    }
    return render(request, 'clndr/update.html', context)

@login_required
def comment_delete(request, meet_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    if request.user == comment.user:
        comment.delete()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))