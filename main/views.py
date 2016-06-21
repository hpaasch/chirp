from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from main.models import Chirp

# class IndexView(TemplateView):
#     template_name = 'index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)  # boilerplate
#         context['all_chirps'] = Chirp.objects.all()
#         return context

class IndexView(ListView):
    template_name = 'index.html'
    model = Chirp   # to here completely replicates what's above

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # boilerplate... ditch the args for super python3!!
        context['amount'] = Chirp.objects.all().count()  # on-the-fly calculations can happen here
        return context
