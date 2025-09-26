from django.shortcuts import render
from django.http import HttpResponse

from todo import models


# Create your views here.
def index(request):
    tasks = models.Task.objects.all()
    return HttpResponse([str(tasks)+'<br/>' for tasks in tasks])
    # return HttpResponse("todo")
    return render(request, 'task.html', {'tasks':tasks})


