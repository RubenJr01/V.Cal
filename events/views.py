from rest_framework import generics
from django.utils.dateparse import parse_datetime
from .models import Event
from .serializers import EventSerializer

class EventListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        qs = Event.objects.all()
        frm = self.request.query_params.get("from")
        to = self.request.query_params.get("to")
        if frm:
            dtf = parse_datetime(frm)
            if dtf:
                qs = qs.filter(start__gte=dtf)
        if to:
            dtt = parse_datetime(to)
            if dtt:
                qs = qs.filter(start__lte=dtt)
        return qs.order_by("start")

class EventRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer