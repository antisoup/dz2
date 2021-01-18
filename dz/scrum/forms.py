from django import forms
from django.utils import timezone

from .models import Project,Task,User

class ProjectForm(forms.Form):
    Name = forms.CharField(label='Название', max_length=255, required=True)
    Description = forms.CharField(label='Описание', max_length=1024, widget=forms.Textarea, required=True)
     
    def save(self):
        project = Project()
        project.name = self.cleaned_data['Name']
        project.description = self.cleaned_data['Description']
        project.created_at = timezone.now()
        project.InsertProject()

        return project

class TaskForm(forms.Form):

    Name = forms.CharField(label='Название', max_length=255, required=True)
    Description = forms.CharField(label='Описание', max_length=1024, widget=forms.Textarea, required=True)
    Size = forms.CharField(label='Размер', max_length=255, required=True, widget=forms.TextInput(attrs={'type':'number'}))
    User = forms.ModelChoiceField(queryset=User.objects.all(), required=True)


    def save(self, pid):
        task = Task()
        task.name = self.cleaned_data['Name']
        task.description = self.cleaned_data['Description']
        task.size = self.cleaned_data['Size']
        task.user = self.cleaned_data.get('User')
        task.project = Project.objects.get(id_project = pid)       
        task.created_at = timezone.now()
        task.InsertTask()

        return task
