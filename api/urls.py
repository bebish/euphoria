from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet

from fragnances.views import FragnanceViewSet

app_name = "api"

router = DefaultRouter()

router.register(r"users", UserViewSet, basename="users")
router.register(r"fragnance", FragnanceViewSet, basename="fragnances")

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("djoser.urls.authtoken")),
]