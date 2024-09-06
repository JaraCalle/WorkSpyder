from django.contrib import admin
from .models import JobFair

@admin.register(JobFair)
class JobFairAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'location', 'organizer')
    list_filter = ('event_date', 'organizer')
    search_fields = ('title', 'description', 'location')
    date_hierarchy = 'event_date'
