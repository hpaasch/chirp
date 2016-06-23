from django.contrib import admin
from main.models import Chirp, StopWord, Profile

class ChirpAdmin(admin.ModelAdmin):
    list_display = ['body', 'bird']
    search_fields = ['body']  # allows search of the body field

admin.site.register(Chirp, ChirpAdmin)


class StopWordAdmin(admin.ModelAdmin):  # to help the non expert maintain the list
    list_display = ['word']
    search_fields = ['word']

admin.site.register(StopWord, StopWordAdmin)

admin.site.register(Profile)
