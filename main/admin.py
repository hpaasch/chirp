from django.contrib import admin

# Register your models here.
from main.models import Chirp, StopWord

class ChirpAdmin(admin.ModelAdmin):
    list_display = ['body', 'bird']
    search_fields = ['body']  # allows search of the body field


class StopWordAdmin(admin.ModelAdmin):  # to help the non expert maintain the list
    list_display = ['word']
    search_fields = ['word']


admin.site.register(Chirp, ChirpAdmin)
admin.site.register(StopWord, StopWordAdmin)
