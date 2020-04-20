from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Member, Play

class MemberCreationForm(UserCreationForm):

    class Meta:
        model = Member
        fields = ('username', 'email', 'first_name', 'last_name', 'description')


class MemberChangeForm(UserChangeForm):

    class Meta:
        model = Member
        fields = ('username', 'email', 'first_name', 'last_name', 'description')


class PlayCreationForm(forms.ModelForm):
    
    class Meta:
        model = Play
        fields = ('title', 'description', 'members', 'awards', 'venues')
