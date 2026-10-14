from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def index(request):
    movies = ["interstellar","gladiator","300 spartanians",'transformers','pirates of caribbean']
    return render(request,'hello/index.html', {'movies': movies})


def about(request):
    goals = [
        "be backend-dev",
        'earn from 150k',
        'work remotely',
        'выучить жанго',
        "сделать свой проект"
    ]
    context = {"goals": goals, "username": "новичок"}
    return render(request, 'hello/about.html', context)

def task_list(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()

    tasks = Task.objects.all().order_by("-created_at")
    return render(request, "hello/task_list.html", {"tasks": tasks, "form": form,})


def done(request):
    tasks = Task.objects.filter(is_done=True)
    return render(request, "hello/task_list.html", {"tasks": tasks})

def active(request):
    tasks = Task.objects.filter(is_done=False).order_by("-created_at")
    return render(request, "hello/task_list.html", {"tasks": tasks})

def task_delete(request, task_id):
    task=get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

def task_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_done=True
    task.save()
    return redirect('task_list')



# Create your views here.