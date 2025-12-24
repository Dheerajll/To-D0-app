from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    added_task = request.POST['task']
    Task.objects.create(task=added_task)
    
    return redirect('home')

def taskCompleted(request,id):
    task = get_object_or_404(Task,pk = id)
    task.is_done = True
    task.save()
    return redirect('home')

def delete_task(request,id):
    task = get_object_or_404(Task,pk =id)
    task.delete()
    return redirect('home')

def unmark(request,id):
    task = get_object_or_404(Task,pk =id)
    task.is_done = False
    task.save()
    return redirect('home')

def editpage(request,id):
    tasks = Task.objects.all()
    edit_task = get_object_or_404(Task,pk = id)
    context = {
        'tasks':tasks,
        'edit_task':edit_task
    }
    if request.method == "POST":
        task = request.POST['task']
        edit_task.task = task
        edit_task.save()
        return redirect('home')
    else:
        return render(request,'editpage.html',context)
