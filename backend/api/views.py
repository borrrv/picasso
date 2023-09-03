from rest_framework.generics import ListAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.status import (HTTP_201_CREATED, HTTP_400_BAD_REQUEST,
                                   HTTP_413_REQUEST_ENTITY_TOO_LARGE)
from rest_framework.views import APIView

from file.models import File
from file.tasks import file_processing

from .serializers import FileSerializer


class UploadApiView(APIView):
    """Upload files"""
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            uploaded_file = file_serializer.validated_data["file"]
            if uploaded_file.size <= 300 * 1024 * 1024:
                file_serializer.save()
                file_id = file_serializer.instance.pk
                file_processing.delay(file_id)
                return Response(file_serializer.data, status=HTTP_201_CREATED)
            else:
                content = {"error": "Max size file 300 Mb"}
                return Response(
                    content, status=HTTP_413_REQUEST_ENTITY_TOO_LARGE
                )
        else:
            return Response(
                file_serializer.errors, status=HTTP_400_BAD_REQUEST
            )


class FileApiView(ListAPIView):
    """Watch all files"""
    queryset = File.objects.all()
    serializer_class = FileSerializer
