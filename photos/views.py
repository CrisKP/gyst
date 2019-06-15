from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo

def index(request):
    return HttpResponse('This is the photos main page')
    
def gallery(request):
    photos = Photo.objects.all()
    return render(request, 'photos/gallery.html', {'photos': photos})
    
def upload(request):
    return render(request, 'photos/upload_form.html', {})
