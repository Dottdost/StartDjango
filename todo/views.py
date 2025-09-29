from gc import get_objects

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from todo import models


# Create your views here.
def index(request):
    tasks = models.Task.objects.all()
    # return HttpResponse([str(tasks) + '<br/>' for tasks in tasks])
    # return HttpResponse("todo")
    return render(request, 'tasks.html', {'tasks': tasks})


def detail(request, task_id):
    task = models.Task.objects.get(pk=task_id)
    return render(request, 'detail.html', {'task': task})


    task = get_object_or_404(models.Task, pk=task_id)
    return render(request, 'detail.html', {'task': task})
