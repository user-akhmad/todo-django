from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from rest_framework import status
from rest_framework import viewsets

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

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    filterset_fields = ['is_done']

    search_fields = ['title', 'description']

    ordering_fields = ['created_at', 'title']




# @api_view(['GET','POST'])
# def api_task_list(request):
#     if request.method == 'GET':
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = TaskSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# class TaskDetailAPIView(APIView):
#     def get(self, request, task_id):
#         task = get_object_or_404(Task, id = task_id)
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)

#     def put(self, request, task_id):
#         task = get_object_or_404(Task, id = task_id)
#         serializer = TaskSerializer(task, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, task_id):
#         task = get_object_or_404(Task, id = task_id)
#         task.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)

# Create your views here.