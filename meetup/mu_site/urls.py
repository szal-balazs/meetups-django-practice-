from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index-page"),
    path("<slug:meetup_slug>/succes", views.confirm_registration, name="reg_confirmation"),
    path("<slug:slug>", views.meetup_detail, name="single-page")
]
