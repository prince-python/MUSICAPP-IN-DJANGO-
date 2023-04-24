from django.shortcuts import render, redirect,HttpResponseRedirect
from .models import Song


def index(request):
    song = Song.objects.all()
    return render(request, 'index.html', {'song': song})



def songpost(request, id):
    song = Song.objects.filter(song_id = id).first()
    return render(request, 'songpost.html', {'song': song})


def upload(request):
    if request.method=='POST':
        name=request.POST['name'] 
        image=request.FILES.get('img')
        audio=request.FILES.get('audio')
        duration=request.POST['dura']
        Song.objects.create(name=name,image=image,audio=audio,duration=duration)
        song = Song.objects.all()
        return HttpResponseRedirect("/")
    else:
        return render(request, 'upload.html')
