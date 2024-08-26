from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import News
from .serializers import NewsSerializer


class NewsViewSet(
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):

    model = News
    queryset = News.objects.all()
    serializer_class = NewsSerializer
