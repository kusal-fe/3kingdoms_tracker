from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="event-tracker-home"),
    path('about/', views.about, name="about"),
]
