from django.contrib import admin
from .models import Person, Musician, Album


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'instrument')

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('artist', 'name')

# Register your models here.
