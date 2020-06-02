from django.urls import path
from . import views

app_name = 'imago'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('add_play/',  views.NewPlayView.as_view(), name="new_play"),
    path('edit_play/<slug:slug>', views.EditPlayView.as_view(), name="edit_play"),
    path('api/plays/', views.play_list_view, name='plays_list'),
    path('api/plays/<slug:slug>', views.play_detail_view, name='play_detail'),
    path('api/members/', views.member_list_view, name='members_list'),
    path('api/members/<slug:slug>', views.member_detail_view, name='member_detail'),
    path('api/venues/', views.member_list_view, name='members_list'),
    path('api/photos/', views.photo_list_view, name='photos_list'),
    path('api/galleries/', views.gallery_list_view, name='gallery_list')
]