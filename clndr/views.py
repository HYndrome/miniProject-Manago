from django.shortcuts import render, redirect
from .models import Meet
from .forms import MeetForm
import json, datetime
from datetime import timedelta, datetime

# Create your views here.
def main(request):
    # Meet.objects.all().delete()

    # 여기서부터
    # Get the current year and month from the URL parameters
    year = int(request.GET.get('year', datetime.today().year))
    month = int(request.GET.get('month', datetime.today().month))

    # Get the first and last days of the month
    first_day = datetime(year, month, 1)
    last_day = datetime(year, month + 1, 1) - timedelta(days=1)

    # Query the database for objects with a date within the month
    my_objects = Meet.objects.filter(date__range=(first_day, last_day))
    # 여기까지

    meet_form = MeetForm()
    context = {
        'meet_form': meet_form,
        'my_objects': my_objects,
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