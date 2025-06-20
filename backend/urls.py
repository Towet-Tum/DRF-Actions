from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from drf_api.views import ItemViewSet

router = DefaultRouter()
router.register(r"items", ItemViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
