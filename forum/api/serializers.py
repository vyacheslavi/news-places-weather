from rest_framework import serializers

from .models import News


class NewsSerializer(serializers.ModelSerializer):

    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = News
        fields = [
            "title",
            "image",
            "text",
            "author",
        ]
