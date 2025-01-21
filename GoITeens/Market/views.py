from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def bootstrap(request):
    return render(request, 'bootstrap.html')

def contact(request):
    return render(request, 'contact.html')

def about_me(request):
    return render(request, 'about_me.html')