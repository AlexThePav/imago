from django import template
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from django.shortcuts import render, reverse

from .forms import MemberCreationForm
from .models import Award, Member, Play, Venue

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

class MembersView(generic.TemplateView):
    template_name = 'imago/members.html'

    def get(self, request, *args, **kwargs):
        context = locals()
        context['title'] = "Members"
        return render(request, self.template_name, context)

class MemberDetailView(generic.TemplateView):
    template_name = 'imago/member_details.html'

    def get(self, request, *args, **kwargs):
        context = locals()
        context['title'] = "Member"
        return render(request, self.template_name, context)

class PlaysView(generic.TemplateView):
    template_name = 'imago/plays.html'

    def get(self, request, *args, **kwargs):
        context = locals()
        context['title'] = "Plays"
        return render(request, self.template_name, context)

class PlayDetailView(generic.TemplateView):
    template_name = 'imago/play_details.html'


    def get(self, request, *args, **kwargs):
        context = locals()
        context['title'] = "Play Details"
        return render(request, self.template_name, context)

class SignUpView(CreateView):
    form_class = MemberCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'