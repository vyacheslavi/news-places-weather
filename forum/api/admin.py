from django.utils.safestring import mark_safe
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from api.models import News


@admin.register(News)
class News(SummernoteModelAdmin):
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
