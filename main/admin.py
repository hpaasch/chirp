from django.contrib import admin

# Register your models here.
from main.models import Chirp

class ChirpAdmin(admin.ModelAdmin):
    list_display = ['body', 'bird']
    search_fields = ['body']  # allows search of the body field 


admin.site.register(Chirp, ChirpAdmin)
