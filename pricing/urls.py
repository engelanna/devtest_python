from django.urls import path, include
from . import views

urlpatterns = [
  path("api/private/login", views.login),
  path("api/private/locations/<slug:country_code>", views.request_1),
  path("api/private/target_groups/<slug:country_code>", views.request_2),
  path("api/private/evaluate_target", views.request_3),

  path("api/public/locations/<slug:country_code>", views.request_4),
  path("api/public/target_groups/<slug:country_code>", views.request_5)
]
