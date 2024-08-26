from django.urls import include, path
from rest_framework import routers


from .views import NewsViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register("news", NewsViewSet, basename="news")

urlpatterns = [
    path("", include(router.urls)),
]
