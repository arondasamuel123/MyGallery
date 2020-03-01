from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

def index(request):
    images = Image.get_images()
    return render(request, 'home.html', {"images":images})

def search_images(request):
    if 'image' in request.GET and request.GET['image']:
       search_word = request.GET.get('image')
       searched_images = Image.search_by_category(search_word)
       message =f"{search_word}"
       return render(request, 'search.html',{"message":message, "images":searched_images})
    else:
        message= "You haven't search anything"
        return render(request, 'search.html', {"message":message})