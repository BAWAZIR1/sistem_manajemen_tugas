from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})


def create_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        status = True if request.POST.get('status') == 'on' else False
        deadline = request.POST['deadline']

        task = Task(title=title, description=description,
                    status=status, deadline=deadline)
        task.save()
        return redirect('task_list')
    return render(request, 'create_task.html')


def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.status = True if request.POST.get('status') == 'on' else False
        task.deadline = request.POST['deadline']

        task.save()
        return redirect('task_list')
    return render(request, 'edit_task.html', {'task': task})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')
