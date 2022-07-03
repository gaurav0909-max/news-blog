from django.urls import path
from . import views

urlpatterns = [
    path('', views.navbar, name="navbar"),
    path('allnews', views.allnews, name="all-news"),
    path('business', views.business, name="business"),
    path('sports', views.sports, name="sports"),
    path('entertainment', views.entertainment, name="entertainment"),
]
