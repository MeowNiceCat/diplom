from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm



def register(request):
    return render(request, 'main/register.html')


def test(request):
    return render(request, 'main/test.html')


def login(request):
    return render(request, 'main/login.html')




def create(request):
    error = ''
    if request.method == 'POST':
       form = TaskForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect('/')
       else:
           error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)