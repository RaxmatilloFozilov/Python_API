from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

# JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


# Swagger
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from config import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Learn DRF",
        default_version='v1',
        description="Django REST framework",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="No License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/python/', include('my_app.urls')),
    path('api/v1/feature/', include('app_python.urls')),
    # Jwt
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
