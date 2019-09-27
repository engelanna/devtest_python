from django.urls import path

from . import views

urlpatterns = [
  path("locations/<slug:country_code>", views.request_1, name="request_1"),
  path("target_groups/<slug:country_code>", views.request_2, name="request_2"),
  path("evaluate_target", views.request_3, name="request_3"),

  path("locations/<slug:country_code>", views.request_4, name="request_4"),
  path("target_groups/<slug:country_code>", views.request_5, name="request_5")
]
