from django import template
from django.http import request, HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, reverse
from django.forms import modelformset_factory
from django.contrib import messages

from .forms import MemberCreationForm, PlayCreationForm
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


class NewPlayView(CreateView):
    form_class = PlayCreationForm
    success_url = reverse_lazy('imago:plays')
    template_name = 'imago/new_play.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('imago.can_add_play'):
            return HttpResponseForbidden()
        return super(NewPlayView, self).dispatch(request, *args, **kwargs)


class EditPlayView(UpdateView):
    model = Play
    fields = ['title', 'cover', 'description', 'members', 'venues', 'awards']
    template_name = 'edit_play.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Edit play"
        return context
