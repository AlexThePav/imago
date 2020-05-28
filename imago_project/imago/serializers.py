from rest_framework import serializers
from .models import Play, Member, Venue, Award


class VenueSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Venue
        fields = ['name', 'location']


class AwardSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Award
        fields = ['name']


class MembersListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Member
        fields = ['slug', 'full_name']


class MemberDetailSerializer(serializers.HyperlinkedModelSerializer):

    awards = AwardSerializer(many=True)

    class Meta:
        model = Member
        fields = ['slug', 'username', 'full_name', 'description', 'awards', 'isImago', 'email', 'facebook', 'instagram'] # to be completed


class PlaysListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Play
        fields = ['slug', 'title', 'description']
    

class PlayDetailSerializer(serializers.HyperlinkedModelSerializer):

    members = MembersListSerializer(many=True)
    venues = VenueSerializer(many=True)
    awards = AwardSerializer(many=True)

    class Meta:
        model = Play
        fields = ['slug', 'title', 'description', 'members', 'venues', 'awards'] # to be completed

