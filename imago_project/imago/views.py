from django import template
from django.http import request, HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, reverse
from django.forms import modelformset_factory
from django.contrib import messages

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from photologue.models import Photo, Gallery

from .forms import MemberCreationForm, PlayCreationForm
from .models import Award, Member, Play, Venue
from .serializers import (PlaysListSerializer, PlayDetailSerializer, 
                            MembersListSerializer, MemberDetailSerializer, 
                            VenueSerializer,
                            ImageGenSerializer, GalleryListSerializer)

@api_view(['GET'])
def play_list_view(request, *args, **kwargs):
    qs = Play.objects.all()
    serializer = PlaysListSerializer(qs, many=True, context={'request':request})
    return Response(serializer.data, status=200)

@api_view(['GET'])
def play_detail_view(request, slug, *args, **kwargs):
    qs = Play.objects.filter(slug=slug)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = PlayDetailSerializer(obj, context={'request':request})
    return Response(serializer.data, status=200)

@api_view(['GET'])
def member_list_view(request, *args, **kwargs):
    qs = Member.objects.all()
    serializer = MembersListSerializer(qs, many=True, context={'request':request})
    return Response(serializer.data, status=200)

@api_view(['GET'])
def member_detail_view(request, slug, *args, **kwargs):
    qs = Member.objects.filter(slug=slug)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = MemberDetailSerializer(obj, context={'request':request})
    return Response(serializer.data, status=200)

@api_view(['GET'])
def venue_list_view(request, *args, **kwargs):
    qs = Venue.objects.all()
    serializer = VenueSerializer(qs, many=True, context={'request':request})
    return Response(serializer.data, status=200)

@api_view(['GET'])
def venue_detail_view(request, slug, *args, **kwargs):
    qs = Venue.objects.filter(slug=slug)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = VenueSerializer(obj, context={'request':request})
    return Response(serializer.data, status=200)

@api_view(['GET'])
def photo_list_view(request, *args, **kwargs):
    qs = Photo.objects.all()
    serializer = ImageGenSerializer(qs, many=True, context={'request':request})
    return Response(serializer.data, status=200)
    
@api_view(['GET'])
def gallery_list_view(request, *args, **kwargs):
    qs = Gallery.objects.all()
    serializer = GalleryListSerializer(qs, many=True, context={'request':request})
    return Response(serializer.data, status=200)

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
