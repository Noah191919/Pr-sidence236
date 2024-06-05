from django.shortcuts import render
from django.contrib.auth.models import User
from . models import *

# Create your views here.


def index(request):
    user = request.user
    events = Event.objects.all()
    album = Album.objects.all()
    activites = Activite.objects.all().order_by('date')
    actus = Actu.objects.all().order_by('date')
    context = {
        'user': user,
        'activites': activites,
        'events': events,
        "album": album, 
        'actus' : actus 
    }
    return render(request, 'index.html', context)