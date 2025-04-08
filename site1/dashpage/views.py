from django.shortcuts import render, redirect,get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.utils import timezone
def dashboard(request):
    todos = Todo.objects.all()
    return render(request, 'dashpage/dashboard.html', {'todos': todos})
@csrf_protect
def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TodoForm()
    context = {
        'form': form,
    }
    return render(request, 'dashpage/create-todo.html', context)
def edit_todo(request, todo_id):
    # waiting for humberto
    return redirect('dashboard')
def start_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.state = 'Active'
    todo.save()
    return redirect('dashboard')
def pause_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.state = "Paused"
    todo.save()
    return redirect('/dashboard')
def stop_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.state = "Stopped"
    todo.save()
    return redirect('/dashboard')
@require_POST
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect('dashboard')
