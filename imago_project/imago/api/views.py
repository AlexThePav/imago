from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from photologue.models import Photo, Gallery
from ..models import Member, Play, Venue
from .serializers import (PlaysListSerializer, PlayDetailSerializer, 
                            MembersListSerializer, MemberDetailSerializer, 
                            VenueSerializer,
                            ImageGenSerializer, GalleryListSerializer)

@api_view(['GET'])
def play_list_view(request):
    qs = Play.objects.all()
    serializer = PlaysListSerializer(qs, many=True, context={'request':request})
    return Response(serializer.data, status=200)

@api_view(['GET'])
def play_detail_view(request, slug):
    try:
        play = Play.objects.get(slug=slug)
    except Play.DoesNotExist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)

    serializer = PlayDetailSerializer(play, context={'request':request})
    return Response(serializer.data)

@api_view(['GET'])
def member_list_view(request):
    qs = Member.objects.all()
    serializer = MembersListSerializer(qs, many=True, context={'request':request})
    return Response(serializer.data, status=200)

@api_view(['GET'])
def member_detail_view(request, slug):
    qs = Member.objects.filter(slug=slug)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = MemberDetailSerializer(obj, context={'request':request})
    return Response(serializer.data, status=200)

@api_view(['GET'])
def venue_list_view(request):
    qs = Venue.objects.all()
    serializer = VenueSerializer(qs, many=True, context={'request':request})
    return Response(serializer.data, status=200)

@api_view(['GET'])
def venue_detail_view(request, slug):
    qs = Venue.objects.filter(slug=slug)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = VenueSerializer(obj, context={'request':request})
    return Response(serializer.data, status=200)

@api_view(['GET'])
def photo_list_view(request):
    qs = Photo.objects.all()
    serializer = ImageGenSerializer(qs, many=True, context={'request':request})
    return Response(serializer.data, status=200)
    
@api_view(['GET'])
def gallery_list_view(request):
    qs = Gallery.objects.all()
    serializer = GalleryListSerializer(qs, many=True, context={'request':request})
    return Response(serializer.data, status=200)
