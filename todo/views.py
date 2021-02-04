from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.

def index(request):
    
    if request.method == "POST":
        newform = TodoForm(request.POST)
        if newform.is_valid():
            newform.save()
            return redirect('/')
    else:
        todolist = Todo.objects.all()
        form = TodoForm()
        context = {
            'todolist' : todolist,
            'form' : form
        }
    return render(request,'index.html',context)

def update(request,pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)
    context = {
        'form' : form
    }
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'update.html', context)    

def delete(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')    