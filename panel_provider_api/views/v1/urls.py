from django.urls import path, include


urlpatterns = [
    path("public/", include(
        "panel_provider_pricing.views.api.v1.public.urls"
    )),
    path("private/", include(
        "panel_provider_pricing.views.api.v1.private.urls"
    )),
]
