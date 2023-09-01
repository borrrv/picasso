from celery import shared_task
from file.models import File


@shared_task
def file_processing(file_id):
    try:
        file = File.objects.get(pk=file_id)
        file.processed = True
        file.save()
        return True
    except Exception as ex:
        raise ex(f"Exception: {ex}")
