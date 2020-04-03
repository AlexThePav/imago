from django.db import models

# Create your models here.
class Show(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  poster = models.ImageField() # read more on this
  members = models.ManyToManyField(Member)
  awards = models.ManyToManyField(Award)
  venues = models.ManyToManyField(Venue)

  def __str__(self):
      return self.title
  

class Member(models.Model):
  name = models.CharField(max_length=200, unique=True)
  description = models.TextField()
  awards = models.ManyToManyField(Award)

  def __str__(self):
      return self.name
  
class Award(models.Model):
  name = models.CharField(max_length=200, unique=True)

class Venue(models.Model):
  name = models.CharField(max_length=200, unique=True)
  location = models.URLField()