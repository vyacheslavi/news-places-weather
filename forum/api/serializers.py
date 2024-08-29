from rest_framework import serializers

from .models import News, Weather


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


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = [
            "temperature",
            "humidity",
            "pressure",
            "wind_direction",
            "wind_speed",
            "place",
            "date",
        ]
