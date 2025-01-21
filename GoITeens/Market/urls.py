from django.contrib import admin
from django.urls import path, include
from Market import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index.html'),
    path('bootstrap', views.bootstrap, name='bootstrap.html'),
    path('contact', views.contact, name='contact.html'),
    path('about_me', views.about_me, name='about_me.html'),
]

urlpatterns += staticfiles_urlpatterns()
