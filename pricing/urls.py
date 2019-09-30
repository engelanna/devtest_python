from django.urls import path
from .views import PublicLocationsView, PublicTargetGroupsView, LoginView, PrivateLocationsView, PrivateTargetGroupsView, PrivatePricingView

urlpatterns = [
    path("api/public/locations/<slug:country_code>",
        PublicLocationsView.as_view(), name="locations"),
    path("api/public/target_groups/<slug:country_code>",
        PublicTargetGroupsView.as_view(), name="target_groups"),

    path("api/private/login", LoginView.as_view(), name="api_login"),

    path("api/private/locations/<slug:country_code>", PrivateLocationsView.as_view()),
    path("api/private/target_groups/<slug:country_code>", PrivateTargetGroupsView.as_view()),
    path("api/private/evaluate_target", PrivatePricingView.as_view()),
]
