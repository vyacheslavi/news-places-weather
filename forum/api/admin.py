from django.utils.safestring import mark_safe
from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from django_admin_geomap import ModelAdmin

from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportActionMixin

from api.models import News, Place, Weather


class PlaceResource(resources.ModelResource):
    class Meta:
        model = Place


class WeatherResource(resources.ModelResource):
    class Meta:
        model = Weather


@admin.register(News)
class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ("text",)
    list_display = (
        "title",
        "image",
        "text",
        "created_at",
        "author",
    )
    search_fields = ("title", "text")
    ordering = ("-created_at",)
    readonly_fields = ["preview_image"]

    def preview_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')


@admin.register(Place)
class PlaceAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = (
        "name",
        "lat",
        "lon",
    )
    search_fields = ("name", "rating")
    ordering = ("-created_at",)

    geomap_default_longitude = "95.1849"
    geomap_default_latitude = "64.2637"
    geomap_default_zoom = "3"
    geomap_height = "500px"

    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"

    resource_class = PlaceResource


@admin.register(Weather)
class WeatherAdmin(ImportExportModelAdmin, ExportActionMixin):
    list_display = (
        "place",
        "temperature",
        "humidity",
        "pressure",
        "wind_direction",
        "wind_speed",
        "date",
    )

    readonly_fields = [field.name for field in Weather._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    list_filter = ("place", "date")
    resource_class = WeatherResource
