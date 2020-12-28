from django.urls import path
from . import views

app_name = 'imago'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('add_play/',  views.NewPlayView.as_view(), name="new_play"),
    path('edit_play/<slug:slug>', views.EditPlayView.as_view(), name="edit_play"),
]