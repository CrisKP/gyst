from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import PhotoForm
from .models import Photo


def index(request):
    return HttpResponse('This is the photos main page')


def gallery(request):
    photos = Photo.objects.all()
    return render(request, 'photos/gallery.html', {'photos': photos})


def upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PhotoForm()
    return render(request, 'photos/upload_form.html', {'form': form})
