from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError


class Event(models.Model):
    title = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="events",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.title} ({self.start} → {self.end})"

    def clean(self):
        """
        Model-level validation. Must be None-safe because admin binds fields
        incrementally and the instance may have start/end = None during clean().
        """
        super().clean()
        if self.start is None or self.end is None:
            return
        if self.start >= self.end:
            raise ValidationError({"end": "End time must be after start time."})