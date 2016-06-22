from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView  # note this import

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


class ChirpDetailView(DetailView):
    # template_name = we can give it a name. OR we can do it the way django wants. created new template dir
    model = Chirp  # this is all needed to show a complete detail view

    def get_queryset(self):
        return Chirp.objects.filter(bird=self.request.user)  # SECURITY CHECK means you can't see others. security issue.
        # can deal with superadmin... 'if' check


class ChirpCreateView(CreateView):
    model = Chirp
    fields = ['body']  # don't include bird, cuz then you can chirp for someone else
    # at just this, it doesn't hook up to the user ForeignKey... do the form_valid
    success_url = '/'

    def form_valid(self, form):
        chirp = form.save(commit=False)   #this half creates it.
        chirp.bird = self.request.user
        return super().form_valid(form)
