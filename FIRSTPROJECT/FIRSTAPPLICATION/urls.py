from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.list, name="index"),
    path("<int:id>", views.home, name="user_page"),
    path("create", views.create, name="create")
]
