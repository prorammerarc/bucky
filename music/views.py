from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Album,Song
from django.template import loader


def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template("music/index.html")
    context = {
        'all_album':all_albums,
    }
    return HttpResponse(template.render(context,request))


def detail(reuest,album_id):
    album = get_object_or_404(Album, pk=album_id)
    context ={
        'album': album,
    }
    template = loader.get_template("music/detail.html")
    return HttpResponse(template.render(context,reuest))


def favourite(request,album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError,Song.DoesNotExist):
        return render(request,"music/detail.html",{
             'album': album,
              'error_message':"you did't selected any Songs"

        })
    else:
        if selected_song.is_favourite is False:
            selected_song.is_favourite = True
        else:
            selected_song.is_favourite = False
        selected_song.save()
        return render(request,"music/detail.html",{"album": album})