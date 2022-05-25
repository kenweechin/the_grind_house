from django.contrib import admin
from . import views
from django.urls import path

from blog.views import frontpage, post_list


urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('<slug:slug>/', views.post_list, name='post_list'),
]