from django.shortcuts import render, redirect, get_object_or_404
from .tasks import create_publication, my_task
from .models import Publication
from celery.result import AsyncResult


def create_publication_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        result = create_publication.delay(title, content)
        return render(request, 'success.html', {'task_id': result.task_id})
    return render(request, 'create_publication.html')


def publication_detail_view(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    return render(request, 'publication_detail.html', {'publication': publication})


def my_view(request):
    if request.method == 'POST':
        return redirect('result')

    return render(request, 'form_template.html')


def result_view(request, result_value=None):
    return render(request, 'result_template.html', {'result_value': result_value})
