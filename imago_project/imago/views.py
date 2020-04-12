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
        context['page_title'] = "Home"
        return render(request, self.template_name, context)

class ContactView(generic.TemplateView):
    template_name = 'imago/contact.html'

    def get(self, request, *args, **kwargs):
        context = locals()
        context['page_title'] = "Contact"
        return render(request, self.template_name, context)

class AboutView(generic.TemplateView):
    template_name = 'imago/about.html'

    def get(self, request, *args, **kwargs):
        context = locals()
        context['page_title'] = "About"
        return render(request, self.template_name, context)

class MembersView(generic.ListView):

    model = Member
    template_name = 'imago/members.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'All members'
        context['all_members_list'] = Member.objects.order_by('first_name')[::]
        return context


class MemberDetailView(generic.DetailView):

    model = Member
    template_name = 'imago/member_details.html'

class PlaysView(generic.ListView):

    model = Play
    template_name = 'imago/plays.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'All plays'
        context['all_plays_list'] = Play.objects.order_by('title')[::]
        return context

class PlayDetailView(generic.DetailView):

    template_name = 'imago/play_details.html'
    model = Play

class SignUpView(CreateView):
    form_class = MemberCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'