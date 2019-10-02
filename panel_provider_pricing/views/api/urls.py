from django.urls import path, include


urlpatterns = [
    path("v1/", include("panel_provider_pricing.views.api.v1.urls")),
]
