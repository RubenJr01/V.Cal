from django.urls import path
from . import views

urlpatterns = [
    path("events/", views.EventListCreateAPIView.as_view(), name="api-events"),
    path("events/<int:pk>/", views.EventRetrieveUpdateDestroyAPIView.as_view(), name="api-event-detail"),
]