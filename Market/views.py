from django.shortcuts import render
from .models import Album, Musician, Person


def index(request):
    return render(request, 'index.html')

def bootstrap(request):
    musicians = Musician.objects.all()
    albums = Album.objects.all()
    person = Person.objects.all()
    return render(request, 'bootstrap.html',
    {'musicians': musicians,
     'albums': albums,
     'person': person,
     })

def contact(request):
    return render(request, 'contact.html')

def about_me(request):
    return render(request, 'about_me.html')