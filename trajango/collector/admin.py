from django.contrib import admin

# Register your models here.
from .models import Device,Location

admin.site.register(Device)
admin.site.register(Location)