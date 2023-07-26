from django.urls import path
from .views import home, logout_view, view

urlpatterns = [
    path("", home, name="home"),
    path("logout", logout_view, name="logout"),
    path("accounts/login", view, name="view"),
]
