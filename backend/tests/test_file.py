import pytest

from file.models import File


@pytest.fixture
def client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def create_file(tmp_path):
    temp_file = tmp_path / "file.txt"
    temp_file.write_text("Hello")
    return temp_file


@pytest.mark.django_db
class TestFile:
    PATH_UPLOAD = "/api/upload/"
    PATH_FILES = "/api/files/"

    def test_upload_file(self, client, create_file):
        initial_file_count = File.objects.count()
        with open(create_file, "rb") as file:
            response = client.post(
                TestFile.PATH_UPLOAD,
                {"file": file},
                format="multipart"
            )
        assert response.status_code == 201
        final_file_count = File.objects.count()
        assert final_file_count == initial_file_count + 1

    def test_file_list(self, client):
        response = client.get(self.PATH_FILES)
        assert response.status_code == 200
