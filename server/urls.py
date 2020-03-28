from django.contrib import admin
from django.urls import path

from server.views import index

urlpatterns = [
    path('graphql/', index),
]
