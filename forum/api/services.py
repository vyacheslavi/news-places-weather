from pyowm import OWM

from django.conf import settings

from .models import Place
from .serializers import WeatherSerializer


def get_weather(place: Place):
    owm = OWM(settings.OWM_API_KEY)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_coords(
        lat=float(place.lat),
        lon=float(place.lon),
    )
    weather = observation.weather
    # longitude latitude
    hhHg_pressure = weather.barometric_pressure().get("press") * 0.750064  # noqa
    # 1 hPa = 0.750064 hhHg
    data = dict(
        temperature=weather.temperature("celsius").get("temp"),
        humidity=weather.humidity,
        pressure=int(hhHg_pressure),
        wind_direction=weather.wind().get("deg"),  # degrees
        wind_speed=weather.wind().get("speed"),  # m / s
        place=place.id,
    )
    return WeatherSerializer(data=data)


def get_weather_from_places():
    places = Place.objects.all()

    for place in places:
        serializer = get_weather(place)
        if serializer.is_valid():
            serializer.save()
