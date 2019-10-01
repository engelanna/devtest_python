from django.urls import path
from .views import PublicLocationsView, PublicTargetGroupsView, LoginView, PrivateLocationsView, PrivateTargetGroupsView, PrivateGetPriceView

urlpatterns = [
    path("public/locations/<slug:country_code>",
        PublicLocationsView.as_view(), name="locations"),
    path("public/target_groups/<slug:country_code>",
        PublicTargetGroupsView.as_view(), name="target_groups"),

    path("private/login", LoginView.as_view(), name="api_login"),

    path("private/locations/<slug:country_code>", PrivateLocationsView.as_view()),
    path("private/target_groups/<slug:country_code>", PrivateTargetGroupsView.as_view()),
    path("private/evaluate_target", PrivateAPIView.as_view()),
]
