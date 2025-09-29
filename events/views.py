from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils.dateparse import parse_datetime
from django.db.models import Q
from .models import Event
from .serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
  queryset = Event.objects.all()
  serializer_class = EventSerializer
  
  def get_queryset(self):
    qs = super().get_queryset()
    frm = self.request.query_params.get('from')
    to = self.request.query_params.get('to')
    
    if frm:
      dtf = parse_datetime(frm)
      if dtf:
        qs = qs.filter(end__gte=dtf)
        
    if to:
      dtt = parse_datetime(to)
      if dtt:
        qs = qs.filter(start__lte=dtt)
    return qs.order_by('start')
  