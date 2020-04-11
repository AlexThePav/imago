from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Member

class MemberCreationForm(UserCreationForm):

    class Meta:
        model = Member
        fields = ('username', 'email', 'first_name', 'last_name',)


class MemberChangeForm(UserChangeForm):

    class Meta:
        model = Member
        fields = ('username', 'email', 'first_name', 'last_name',)
        