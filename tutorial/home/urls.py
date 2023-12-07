from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index, name='index'),
    path("show/", views.show, name='show'),
    path("add/", views.add, name='add'),
    path("delete/<int:id>/", views.delete, name='delete'),
    path("update/<int:id>/", views.update, name='update'),
]
