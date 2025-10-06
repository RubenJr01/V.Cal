from django.contrib import admin
from django import forms
from .models import Event


class EventAdminForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "start", "end"]  # omit 'owner' – we set it in save_model
        widgets = {
            "start": forms.SplitDateTimeWidget(
                date_attrs={"type": "date"},
                time_attrs={"type": "time"},
            ),
            "end": forms.SplitDateTimeWidget(
                date_attrs={"type": "date"},
                time_attrs={"type": "time"},
            ),
        }

    def clean(self):
        cleaned = super().clean()
        start = cleaned.get("start")
        end = cleaned.get("end")
        # Form-level validation for friendlier admin error messages
        if start and end and start >= end:
            self.add_error("end", "End time must be after start time.")
        return cleaned


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm
    list_display = ("title", "start", "end", "owner")
    fields = ("title", "start", "end")  # don't expose owner in the form

    def save_model(self, request, obj, form, change):
        # Automatically set owner if not already set
        if not obj.owner_id:
            obj.owner = request.user
        super().save_model(request, obj, form, change)