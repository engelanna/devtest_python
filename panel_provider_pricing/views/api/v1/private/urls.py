from .get_price_view import GetPriceView
from .login_view import LoginView
from .locations_view import LocationsView
from .target_groups_view import TargetGroupsView


urlpatterns = [
    path("login/", LoginView.as_view(), name="api_v1_private_login"),
    path("locations/<slug:country_code>/", LocationsView.as_view(),
        name="api_v1_private_locations"),
    path("locations/<slug:country_code>/", TargetGroupsView.as_view(),
        name="api_v1_private_target_groups"),
    path("evaluate_target/", GetPriceView.as_view()),
]
