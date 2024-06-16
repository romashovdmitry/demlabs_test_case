# Django imports
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

# Swagger imports
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)

# import config, constants data
from main.settings import MEDIA_ROOT, MEDIA_URL, STATIC_URL, STATIC_ROOT

# import views, custom foos, classes
from main.views import health_check


urlpatterns = [
    # for docker health-checker
    path('/', health_check),
    # Swagger urls
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    # admin url
    path("admin/", admin.site.urls),
    # projects urls
    path("api/v1/user/", include("user.urls")),
    path("api/v1/products/", include("product.urls")),
    path("api/v1/order/", include("order.urls")),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)