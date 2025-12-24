from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    added_task = request.POST['task']
    Task.objects.create(task=added_task)
    
    return redirect('home')
