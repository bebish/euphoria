from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from users.views import UserViewSet
from fragnances.views import FragnanceViewSet

app_name = "api"

router = DefaultRouter()

router.register(r"users", UserViewSet, basename="users")
router.register(r"fragnance", FragnanceViewSet, basename="fragnances")

schema_view = get_schema_view(
    openapi.Info(
        title="EUPHORIA API",
        default_version='v1',
        description="EUPHORIA API",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="У НАС НЕТ ЛИЦЕНЗИИ ДЕЛАЕМ ЧТО ХОТИМ"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]
