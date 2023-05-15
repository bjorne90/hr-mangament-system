from django.contrib import admin
from .models import WorkShift

class WorkShiftAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time', 'is_booked', 'role')
    list_display_links = ('name',)  # Add the field you want to link to the change view

admin.site.register(WorkShift, WorkShiftAdmin)
