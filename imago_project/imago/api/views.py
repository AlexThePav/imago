from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from photologue.models import Photo, Gallery
from ..models import Member, Play, Venue
from .serializers import (PlaysListSerializer, PlayDetailSerializer, 
                            MembersListSerializer, MemberDetailSerializer, 
                            VenueSerializer,
                            ImageGenSerializer, GalleryListSerializer)


@api_view(['GET', 'PUT', 'DELETE'])
def play_detail(request, slug, format=None):
    '''
    Retrieve, update or delete a play
    '''
    try:
        play = Play.objects.get(slug=slug)
    except Play.DoesNotExist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlayDetailSerializer(play)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PlayDetailSerializer(play, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        play.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def play_list(request, format=None):
    '''
    List all plays, or create a new play.
    '''
    if request.method == 'GET':
        plays = Play.objects.all()
        serializer = PlaysListSerializer(plays, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PlaysListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def member_list(request):
    qs = Member.objects.all()
    serializer = MembersListSerializer(qs, many=True, context={'request':request})
    return Response(serializer.data, status=200)

@api_view(['GET'])
def member_detail(request, slug):
    qs = Member.objects.filter(slug=slug)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = MemberDetailSerializer(obj, context={'request':request})
    return Response(serializer.data, status=200)

@api_view(['GET'])
def venue_list(request):
    qs = Venue.objects.all()
    serializer = VenueSerializer(qs, many=True, context={'request':request})
    return Response(serializer.data, status=200)

@api_view(['GET'])
def venue_detail(request, slug):
    qs = Venue.objects.filter(slug=slug)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = VenueSerializer(obj, context={'request':request})
    return Response(serializer.data, status=200)

@api_view(['GET'])
def photo_list(request):
    qs = Photo.objects.all()
    serializer = ImageGenSerializer(qs, many=True, context={'request':request})
    return Response(serializer.data, status=200)
    
@api_view(['GET'])
def gallery_list(request):
    qs = Gallery.objects.all()
    serializer = GalleryListSerializer(qs, many=True, context={'request':request})
    return Response(serializer.data, status=200)
