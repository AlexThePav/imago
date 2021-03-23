import os
from rest_framework import serializers

from ..models import Play, Member, Venue, Award
from photologue.models import Photo, Gallery

class ImageGenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    slug = serializers.SlugField(max_length=250)
    thumbnail = serializers.SerializerMethodField()
    display = serializers.SerializerMethodField()

    def create(self, validated_data):
        """
        Create and return a new `Photo` instance, given the validated data.
        """
        return Photo.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Photo` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance
    
    def get_thumbnail(self, obj):
        filename = obj.image_filename()
        file_extension = os.path.splitext(filename)[1]
        file_noext = os.path.splitext(filename)[0]
        return file_noext + "_thumbnail" + file_extension
    
    def get_display(self, obj):
        filename = obj.image_filename()
        file_extension = os.path.splitext(filename)[1]
        file_noext = os.path.splitext(filename)[0]
        return file_noext + "_display" + file_extension


class GalleryListSerializer(serializers.HyperlinkedModelSerializer):

    photos = ImageGenSerializer(many=True)

    class Meta:
        model = Gallery
        fields = ['title',]


class GalleryDetailSerializer(serializers.HyperlinkedModelSerializer):

    photos = ImageGenSerializer(many=True)

    class Meta:
        model = Gallery
        fields = ['title', 'photos']


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
        fields = ['slug', 'get_profile_pic', 'full_name']


class MemberDetailSerializer(serializers.HyperlinkedModelSerializer):
    awards = AwardSerializer(many=True)

    class Meta:
        model = Member
        fields = ['slug', 'username', 'full_name', 'description', 'awards', 'isImago', 'email', 'facebook', 'instagram']


class PlaysListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Play
        fields = ['slug', 'get_cover', 'title', 'description']
    

class PlayDetailSerializer(serializers.HyperlinkedModelSerializer):

    members = MembersListSerializer(many=True)
    venues = VenueSerializer(many=True)
    awards = AwardSerializer(many=True)
    gallery = GalleryDetailSerializer()

    class Meta:
        model = Play
        fields = ['slug', 'get_cover', 'gallery', 'title', 
                    'description', 'members', 'venues', 'awards']

