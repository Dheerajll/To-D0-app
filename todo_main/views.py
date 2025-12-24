from django.shortcuts import render
from django.http import HttpResponse
from todo.models import Task


def home(request):
    tasks = Task.objects.all().order_by('-created_at')
    context ={
        'tasks':tasks
    }
    return render(request,'home.html',context)
