from django.urls import path
from . import webviews
from .import views

urlpatterns = [
  path("", webviews.home, name="home"),
  path("signup/", webviews.signup_view, name="signup"),
  path("dashboard/", webviews.dashboard, name="dashboard"),
  path("calendar", webviews.calendar, name="calendar"),
  path("about/", webviews.about, name="about"),
  path("login/", webviews.login_view, name="login"),
  path("logout/", webviews.logout_view, name="logout"),
]