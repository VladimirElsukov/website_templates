from django.urls import path
from . import views

urlpatterns = [
    path("", views.recipe_view, name="recipe_view"),
    path("recipe", views.recipe_view, name="recipe_view"),
]
