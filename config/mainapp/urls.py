from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello_world, name="hello_world"),
    path("<slug:lang>/", views.language, name="language"),
]
