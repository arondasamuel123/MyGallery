from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, Location

def index(request):
    images = Image.get_images()
    locations = Location.objects.all()
    return render(request, 'home.html', {"images":images, "locations":locations})

def search_images(request):
    if 'image' in request.GET and request.GET['image']:
       search_word = request.GET.get('image')
       searched_images = Image.search_by_category(search_word)
       message =f"{search_word}"
       return render(request, 'search.html',{"message":message, "images":searched_images})
    else:
        message= "You haven't search anything"
        return render(request, 'search.html', {"message":message})
    
def filter_by_loc(request, img_location):
    loc = Location.get_loc_by_ID(img_location)
    images = Image.filter_by_location(img_location)
    message =f"{loc.image_location}"
    return render(request, 'location.html',{"images":images, "message":message})