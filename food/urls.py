from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include,path
from django.views.generic.base import TemplateView

urlpatterns = [
    path("", views.add_food, name="add_food"),
]