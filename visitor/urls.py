from django.urls import path
from . import views

urlpatterns = [
    path("main/", views.main),
    path("list/", views.visitor_list),
    path("search/", views.visitor_search),
    path("add/", views.visitor_add),
    path("<int:visitor_id>/", views.visitor_detail),
    path("exit/<int:id>/", views.visitor_exit),
    # path("exit/", views.visitor_exit),
]
