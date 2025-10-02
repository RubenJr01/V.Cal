from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from events.views import EventViewSet

router = DefaultRouter()
router.register(r"events", EventViewSet, basename="event")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),   # /api/events/
    path("", include("events.urls")),     # base HTML page
]