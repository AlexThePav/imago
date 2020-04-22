from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _


class Venue(models.Model):
    name = models.CharField(max_length=200, unique=True)
    location = models.URLField()

    def __str__(self):
        return self.name


class Award(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Member(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    isImago = models.BooleanField(default=False)
    #   date_of_birth = models.DateTimeField(auto_now=False)
    email = models.EmailField(_('email address'), unique=True)
    facebook = models.URLField()
    instagram = models.URLField()
    awards = models.ManyToManyField(Award)
    slug = models.SlugField(null=False, unique=True)

    def get_absolute_url(self):
        return reverse("member_detail", kwargs={"slug": self.slug})
    
    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.get_full_name())
        super(Member, self).save(*args, **kwargs)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class Play(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    cover = models.ImageField(upload_to='images/', default=None, null=True, blank=True)
    members = models.ManyToManyField(get_user_model())
    awards = models.ManyToManyField(Award)
    venues = models.ManyToManyField(Venue)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("play_detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Play, self).save(*args, **kwargs)


def get_play_image_folder_name(instance):
        return "images/%s" % (instance.title)


class Image(models.Model):
    play = models.ForeignKey('Play', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_play_image_folder_name, blank=True, null=True)
