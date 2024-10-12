from django.contrib import admin
from .models import JobFair

@admin.register(JobFair)
class JobFairAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_event_date', 'end_event_date', 'start_hour', 'end_hour', 'department', 'city', 'direction', 'keynote_speaker', 'image')
    list_filter = ('start_event_date', 'department', 'city')
    date_hierarchy = 'start_event_date'
