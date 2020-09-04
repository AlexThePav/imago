from rest_framework import serializers
from .models import Play, Member, Venue, Award
from photologue.models import Photo, Gallery


class PhotoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Photo
        fields = ['get_absolute_url', 'image_filename', 'cache_url']


class GalleryListSerializer(serializers.HyperlinkedModelSerializer):

    photos = PhotoSerializer(many=True)

    class Meta:
        model = Gallery
        fields = ['slug', 'title', 'get_absolute_url']


class GalleryDetailSerializer(serializers.HyperlinkedModelSerializer):

    photos = PhotoSerializer(many=True)

    class Meta:
        model = Gallery
        fields = ['slug', 'title', 'get_absolute_url', 'photos']

class VenueSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Venue
        fields = ['id', 'name', 'location']


class AwardSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Award
        fields = ['id', 'name']


class MembersListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Member
        fields = ['slug', 'full_name']


class MemberDetailSerializer(serializers.HyperlinkedModelSerializer):

    awards = AwardSerializer(many=True)

    class Meta:
        model = Member
        fields = ['slug', 'username', 'full_name', 'description', 'awards', 'isImago', 'email', 'facebook', 'instagram']


class PlaysListSerializer(serializers.HyperlinkedModelSerializer):
    cover = PhotoSerializer()

    class Meta:
        model = Play
        fields = ['slug', 'cover', 'title', 'description']
    

class PlayDetailSerializer(serializers.HyperlinkedModelSerializer):

    members = MembersListSerializer(many=True)
    venues = VenueSerializer(many=True)
    awards = AwardSerializer(many=True)
    gallery = GalleryDetailSerializer()
    cover = PhotoSerializer()

    class Meta:
        model = Play
        fields = ['slug', 'cover', 'title', 'description', 'members', 'venues', 'awards', 'gallery'] # to be completed

