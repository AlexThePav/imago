from django.urls import path
from . import views

app_name = 'imago'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('members/', views.MembersView.as_view(), name='members'),
    path('members/<slug:slug>', views.MemberDetailView.as_view(), name='member_detail'),
    path('plays/', views.PlaysView.as_view(), name='plays'),
    path('plays/<slug:slug>', views.PlayDetailView.as_view(), name='play_detail'),
    path('signup/', views.SignUpView.as_view(), name='signup')
]