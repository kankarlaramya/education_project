from django.shortcuts import render
from django.http import HttpResponse
from .models import task
from django.template import loader

# Create your views here.
def index(request):
    task_list = task.objects.all()
    template = loader.get_template('education/index.html')
    context ={
        'task_list':task_list,
    }
    return render(request,'education/index.html',context)


def detail(request,task_id):
    task = task.objects.get(pk = task_id)
    context ={
        'task':task,
    }
    return render(request, 'education/detail.html', context)
