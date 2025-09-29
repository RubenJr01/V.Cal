from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from events.views import EventViewSet
from django.urls import path
from . import webviews


router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')

urlpatterns = [
  path('admin/', admin.site.urls),
  path('api/', include(router.urls)),
  path('', include('events.url')),
  path('', webviews.base, name='base'),
]