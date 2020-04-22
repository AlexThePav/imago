from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Member, Play, Image

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
        fields = ('title', 'cover', 'description', 'members', 'awards', 'venues')


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Image
        fields = ('play', 'image',)