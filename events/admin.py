from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
  list_display = ('title', 'start', 'end', 'all_day')
  search_fields = ('title',)
  list_filter = ('all_day',)
