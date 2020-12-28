from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ..api import views

app_name = 'imago'
urlpatterns = [
    path('plays/', views.play_list, name='plays_list'),
    path('plays/<slug:slug>', views.play_detail, name='play_detail'),
    path('members/', views.member_list, name='members_list'),
    path('members/<slug:slug>', views.member_detail, name='member_detail'),
    path('venues/', views.member_list, name='members_list'),
    path('photos/', views.photo_list, name='photos_list'),
    path('galleries/', views.gallery_list, name='gallery_list')
]

urlpatterns = format_suffix_patterns(urlpatterns)