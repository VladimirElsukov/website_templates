from django.urls import path
from . import views

urlpatterns = [
    path("", views.sport, name="sport"),
    path("<slug:sp>/", views.nav_sport, name="sport"),
]
