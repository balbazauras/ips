from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(System)
admin.site.register(Sensor)
admin.site.register(Technician, UserAdmin)
admin.site.register(DataEntry)
