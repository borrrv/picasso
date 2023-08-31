from django.db import models


class File(models.Model):
    file = models.FileField("File", upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    class Meta:
        ordering = ("-uploaded_at",)
        verbose_name = "File"
        verbose_name_plural = "Files"

    def __str__(self):
        return self.file.name
