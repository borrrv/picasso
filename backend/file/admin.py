from django.contrib import admin
from .models import File


class FileAdmin(admin.ModelAdmin):
    list_display = (
        "file",
        "uploaded_at",
        "processed",
    )
    list_filter = (
        "file",
        "uploaded_at",
        "processed",
    )
    search_fields = ("file",)


admin.site.register(File, FileAdmin)
