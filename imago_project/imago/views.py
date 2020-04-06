from django.shortcuts import render, reverse
from django.views import generic
from django import template
from .models import Award, Member, Show, Venue


# index will become generic.ListView
class IndexView(generic.TemplateView):
    template_name = 'imago/index.html'

    def get(self, request, *args, **kwargs):
        context = locals()
        context['title'] = "Home"
        return render(request, self.template_name, context)

class ContactView(generic.TemplateView):
    template_name = 'imago/contact.html'

    def get(self, request, *args, **kwargs):
        context = locals()
        context['title'] = "Contact"
        return render(request, self.template_name, context)

class AboutView(generic.TemplateView):
    template_name = 'imago/about.html'

    def get(self, request, *args, **kwargs):
        context = locals()
        context['title'] = "About"
        return render(request, self.template_name, context)