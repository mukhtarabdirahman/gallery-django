from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image
# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def pics_of_day(request):
    date = dt.date.today()
    display=Image.objects.all()
    return render(request, 'all-pics/today-pics.html', {"display": display,})
def convert_dates(dates):
    
    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day
def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_image_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-pics/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pics/search.html',{"message":message})
    
    
