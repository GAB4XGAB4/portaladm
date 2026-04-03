from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('api/humor/', views.humor_api, name='humor_api'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]