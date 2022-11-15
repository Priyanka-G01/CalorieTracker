from django.contrib import admin
from django.urls import path, include
from .views import workout
urlpatterns = [
   path('workout/',workout, name='workout'),
]