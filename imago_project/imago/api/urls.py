from django.urls import path

from ..api import views

app_name = 'imago'
urlpatterns = [
    path('plays/', views.play_list_view, name='plays_list'),
    path('plays/<slug:slug>', views.play_detail_view, name='play_detail'),
    path('members/', views.member_list_view, name='members_list'),
    path('members/<slug:slug>', views.member_detail_view, name='member_detail'),
    path('venues/', views.member_list_view, name='members_list'),
    path('photos/', views.photo_list_view, name='photos_list'),
    path('galleries/', views.gallery_list_view, name='gallery_list')
]