from rest_framework import serializers
from .models import Play, Member, Venue, Award


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
        fields = [
            'slug', 'username', 'full_name', 'description', 'awards',
            'isImago', 'email', 'facebook', 'instagram'
        ]


class PlaysListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Play
        fields = ['slug', 'get_cover', 'title', 'description']


class PlayDetailSerializer(serializers.HyperlinkedModelSerializer):

    members = MembersListSerializer(many=True)
    venues = VenueSerializer(many=True)
    awards = AwardSerializer(many=True)

    class Meta:
        model = Play
        fields = [
            'slug', 'get_cover', 'title', 'description',
            'members', 'venues', 'awards'
            ]

