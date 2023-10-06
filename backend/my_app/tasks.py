from .models import Publication
from celery import shared_task


@shared_task
def create_publication(title, content):
    publication = Publication.objects.create(title=title, content=content)
    return publication.id


@shared_task
def my_task(arg1, arg2):
    result = arg1 + arg2
    return result

