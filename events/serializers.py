from rest_framework import serializers
from .models import Event
import uuid
from django.utils import timezone

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = ['id', 'title', 'description', 'location', 'all_day', 'start', 'end', 'created_at', 'updated_at']
    read_only_fields = ['created_at', 'updated_at']
    
    def validate(self, data):
      start = data.get('start', getattr(self.instance, 'start', None))
      end = data.get('end', getattr(self.instance, 'end', None))
      if start and end and start >= end:
        raise serializers.ValidationError({'end': 'start must be before end'})
      return data
    
    def create(self, validated_data):
      if 'id' not in validated_data or not validated_data['id']:
        validated_data['id'] = str(uuid.uuid4())
      return super().create(validated_data)