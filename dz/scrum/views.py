from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, reverse
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.

from .models import Project, Task
from .forms import ProjectForm,TaskForm


def ProjectList(request):
    project_list = Project.GetAllProjects()
    template = loader.get_template('index.html')
    context =  {
        'project_list': project_list,
    }
    return HttpResponse(template.render(context))

def project_tasks(request, project_id):
    template = loader.get_template('project.html')
    task_list = Task.objects.filter(project=Project.objects.get(id_project = project_id))
    #task_list = get_list_or_404(Task, project_id=project_id)
    return render(request, 'project.html', {'task_list': task_list, 'project': project_id})
    
def task_detail(request, project_id, id):
    template = loader.get_template('task_detail.html')
    task = Task.objects.get(id_task=id)    
    return render(request, 'task_detail.html', {'task': task})

def ProjectNew(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES) 
        if form.is_valid():
            project = form.save()
            project.save() 
            return redirect('projects')
    else:
        form = ProjectForm()
    return render(request, 'project_new.html', {'form': form})

def task_new(request, project_id):
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES) 
        if form.is_valid():
            task = form.save(project_id)
            task.save(project_id) 
            return redirect(reverse('project_tasks', kwargs={"project_id": project_id}))
    else:
        form = TaskForm()
    return render(request, 'task_new.html', {'form': form})


      
    
    