from django.urls import path, include

from .login_view import LoginView
from .locations_view import LocationsView
from .panel_price_view import PanelPriceView
from .target_groups_view import TargetGroupsView


urlpatterns = [
    path(
        "login/", LoginView.as_view(), name="api_v1_private_login"
    ),
    path(
        "locations/<slug:country_code>/", LocationsView.as_view(), name="api_v1_private_locations"
    ),
    path(
        "target_groups/<slug:country_code>/", TargetGroupsView.as_view(), name="api_v1_private_target_groups"),
    path(
        "evaluate_target/", PanelPriceView.as_view(), name="api_v1_private_evaluate_target"
    ),
]
