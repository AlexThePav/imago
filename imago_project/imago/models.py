from datetime import date
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

from photologue.models import Gallery

import os



class Venue(models.Model):
    name = models.CharField(max_length=200, unique=True)
    location = models.URLField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Award(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Member(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    profile_pic = models.ImageField('image', 
                                    upload_to='profile_pics', 
                                    null=True, 
                                    blank=True)
    description = models.TextField()
    isImago = models.BooleanField(default=False)
    email = models.EmailField(_('email address'), unique=True)
    facebook = models.URLField()
    instagram = models.URLField()
    awards = models.ManyToManyField(Award)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("member_detail", kwargs={"slug": self.slug})
    
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)
    
    def get_profile_pic(self):
        return os.path.dirname(self.profile_pic.url) + "/" + os.path.basename(self.profile_pic.name)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.get_full_name())
        super(Member, self).save(*args, **kwargs)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class Play(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    cover = models.ImageField('image', 
                                upload_to='covers', 
                                default=None, 
                                null=True)
    gallery = models.OneToOneField(Gallery, on_delete=SET_NULL, null=True, blank=True)
    members = models.ManyToManyField(get_user_model())
    awards = models.ManyToManyField(Award)
    venues = models.ManyToManyField(Venue)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("play_detail", kwargs={"slug": self.slug})

    def get_cover(self):
        return os.path.dirname(self.cover.url) + "/" + os.path.basename(self.cover.name)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Play, self).save(*args, **kwargs)