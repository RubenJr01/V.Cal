from django.db import models
from django.core.exceptions import ValidationError

class Event(models.Model):
  id = models.CharField(primary_key=True, max_length=36, editable=False)
  title = models.CharField(max_length=200)
  description = models.TextField(blank=True, null=True)
  location = models.CharField(max_length=255, blank=True, null=True)
  all_day = models.BooleanField(default=False)
  start = models.DateTimeField()
  end = models.DateTimeField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    indexes = [
      models.Index(fields=['start']),
      models.Index(fields=['end']),
    ]
    ordering = ['start']
    
  def __str__(self):
    return f"{self.title} ({self.start} -> {self.end})"
  
  def clean(self):
    if self.start >= self.end:
      raise ValidationError({'end': 'start must be before end'})
