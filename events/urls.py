from django.urls import path
from . import webviews

urlpatterns = [ path("", webviews.base, name="base"), ]