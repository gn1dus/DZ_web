from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("name/", views.name, name="name"),
    path("group", views.name,name="group"),
    path("age", views.name,name="age"),
    path("common", views.name,name="common"),
]