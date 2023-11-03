from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view),
    path("logout/", views.logout_view),
    path("signup/", views.signup),
    path("delete/", views.delete),
    path("my_page/", views.my_page),
]
