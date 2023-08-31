from django.urls import path

from .views import FileApiView, UploadApiView

urlpatterns = [
    path("upload/", UploadApiView.as_view()),
    path("files/", FileApiView.as_view()),
]
