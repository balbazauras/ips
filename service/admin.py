from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class DataEntryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DataEntry._meta.get_fields()]


admin.site.register(System)
admin.site.register(Sensor)
admin.site.register(Technician, UserAdmin)
admin.site.register(DataEntry, DataEntryAdmin)


