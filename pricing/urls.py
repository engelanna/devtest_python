from django.urls import path
from rest_framework import renderers
from . import views
# PrivateAPIView.as_view({
#   "post": "create",
#   "get": "list",
# })

# PublicAPIView.as_view({
#     "get": "retrieve",
#     "put": "update",
#     "patch": "partial_update",
#     "delete": "destroy"
# })
# snippet_highlight = SnippetViewSet.as_view({
#     "get": "highlight"
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     "get": "list"
# })
# user_detail = UserViewSet.as_view({
#     "get": "retrieve"
# })

urlpatterns = [
  path("api/private/login", views.PrivateAPILogin.as_view()),
  path("api/private/locations/<slug:country_code>", views.request_1),
  path("api/private/target_groups/<slug:country_code>", views.request_2),
  path("api/private/evaluate_target", views.request_3),

  path("api/public/locations/<slug:country_code>", views.request_4),
  path("api/public/target_groups/<slug:country_code>", views.request_5)
]
