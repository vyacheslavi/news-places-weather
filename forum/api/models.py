from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from django_admin_geomap import GeoItem


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    image = models.ImageField(
        upload_to=r"news_images/%Y/%m/%d/",
        default=None,
        blank=True,
        null=True,
        verbose_name="Главное изображение",
    )
    text = models.TextField(max_length=500, verbose_name="Текст новости")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    author = models.ForeignKey(
        User,
        blank=True,
        on_delete=models.CASCADE,
        related_name="posted_news",
        verbose_name="Автор",
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "news"

    def __unicode__(self):
        return str(self.about_desc)


class Place(models.Model, GeoItem):
    name = models.CharField(
        max_length=50,
        verbose_name="Название места",
        unique=True,
    )
    lon = models.FloatField(verbose_name="Долгота")
    lat = models.FloatField(verbose_name="Широта")
    rating = models.IntegerField(
        validators=[
            MaxValueValidator(25),
            MinValueValidator(0),
        ],
        default=0,
        verbose_name="Рейтинг",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        ordering = ("-created_at",)

    @property
    def geomap_longitude(self):
        return str(self.lon)

    @property
    def geomap_latitude(self):
        return str(self.lat)
