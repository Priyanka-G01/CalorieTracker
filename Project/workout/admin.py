from django.contrib import admin
from .models import Workout, CaloriesLostInDay

# Register your models here.
admin.site.register(Workout)
admin.site.register(CaloriesLostInDay)