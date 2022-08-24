from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Snack  # thing in demo

admin.site.register(Snack)
