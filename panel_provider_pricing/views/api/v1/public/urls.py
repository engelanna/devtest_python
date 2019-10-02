from django.urls import path, include

from .locations_view import LocationsView
from .target_groups_view import TargetGroupsView


urlpatterns = [
        path("locations/<slug:country_code>/", LocationsView.as_view(),
            name="api_v1_public_locations"),
        path("locations/<slug:country_code>/", TargetGroupsView.as_view(),
            name="api_v1_public_target_groups"),
]
