from django.shortcuts import render, redirect
from .models import Meet
from .forms import MeetForm
import json, datetime
from datetime import timedelta, datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count

# Create your views here.

def main(request):
    # Meet.objects.all().delete()

    meet_form = MeetForm()
    context = {
        'meet_form': meet_form,
    }
    return render(request, 'clndr/main.html', context)

def meet(request):
    # Get the selected date data from the form
    selected_date = request.POST.get('selected-date')
    if selected_date is not None:
        selDate = json.loads(selected_date)
    meet_form = MeetForm(request.POST)
    if meet_form.is_valid():
        meet = meet_form.save(commit=False)
        meet.user = request.user
        print(selDate)
        meet.date = selDate
        meet.save()
        return redirect('clndr:main')
    
def detail(request, urlDate):
    meets = Meet.objects.filter(date=urlDate)
    context = {
        'meets': meets,
    }
    return render(request, 'clndr/detail.html', context)

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