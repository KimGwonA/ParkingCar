from django.urls import path
from . import views

urlpatterns = [
    path("feeds/", views.feeds),
]
