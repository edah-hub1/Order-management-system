from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders.views import CustomerViewSet, OrderViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Initialize Default Router
router = DefaultRouter()
router.register(r"customers", CustomerViewSet)
router.register(r"orders", OrderViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/", include(router.urls)
    ),  # Prefixing API routes with 'api/' for better structure
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
