from django.db import models
from django.http import HttpRequest
import sqlite3

# Create your models here.

class Project(models.Model):
    id_project = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Название проекта')
    description = models.TextField(max_length = 1024, verbose_name= 'Описание проекта')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    @staticmethod
    def GetAllProjects():
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        sql = 'SELECT * FROM scrum_project'        
        c.execute(sql)
        project = c.fetchall()
        c.close()
        conn.close()
        return project
    
        
    def InsertProject(self):
        project = ProjectAR(self.id_project, self.name, self.description, self.created_at)
        project.insertProject()       
        

class ProjectAR:
    
    def __init__(self, id_project, name, description, created_at):
        self.id_project = None
        self.name = None
        self.description = None
        self.created_at = None
    
    def GetProject(self): #####################################################################
        conn = sqlite3.connect('scrum.sqlite3')
        c = conn.cursor()        
        sql = 'SELECT * FROM scrum_project WHERE id_project = %s' % str(self.id_project)
        c.execute(sql)
        project = c.fetchall()
        c.close()
        conn.close()
        return project

    def insertProject(self):        
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        args = {'pn': str(self.name), 'pd': str(self.description), 'pc': str(self.created_at)}
        sql = "INSERT INTO scrum_project (name, description, created_at) VALUES ('%(pn)s', '%(pd)s', '%(pc)s')" % args
        c.execute(sql)
        c.close()
        conn.close()        

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name='Название задачи')
    password = models.CharField(max_length=10, verbose_name='Пароль')

    def __str__(self):
        return self.name
    
    def GetUser(self): #####################################################################
        conn = sqlite3.connect('scrum.sqlite3')
        c = conn.cursor()        
        sql = 'SELECT * FROM scrum_user WHERE id_user = %s' % str(self.id_user)
        c.execute(sql)
        project = c.fetchall()
        c.close()
        conn.close()
        return project

class Task(models.Model):
    id_task = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Название задачи')
    description = models.TextField(max_length = 1024, verbose_name= 'Описание задачи')
    size = models.IntegerField(verbose_name='Размер задачи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='TaskProject')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='TaskUser')

    def __str__(self):
        return self.name

    @staticmethod
    def GetAllProjectTasks(project_id):
        tasks = Task.objects.filter(project=project_id)
        return tasks

    def GetTask(id): #####################################################################
        task = Task.objects.get(id_task = id)
        return task    
    
    def InsertTask(self):        
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        args = {'tn': str(self.name), 'td': str(self.description), 'ts':str(self.size), 'tc': str(self.created_at), 'tp': str(self.project.id_project), 'tu': str(self.user.id_user)}
        sql = "INSERT INTO scrum_task (name, description, size, created_at, project_id, user_id) VALUES ('%(tn)s', '%(td)s', '%(ts)s', '%(tc)s', '%(tp)s', '%(tu)s')" % args
        c.execute(sql)
        c.close()
        conn.close() 


class Task(models.Model):
    id_task = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Название задачи')
    description = models.TextField(max_length = 1024, verbose_name= 'Описание задачи')
    size = models.IntegerField(verbose_name='Размер задачи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='TaskProject')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='TaskUser')

    def __str__(self):
        return self.name

    @staticmethod
    def GetAllProjectTasks(project_id):
        tasks = Task.objects.filter(project=project_id)
        return tasks

    def GetTask(id): #####################################################################
        task = Task.objects.get(id_task = id)
        return task    
    
    def InsertTask(self):        
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        args = {'tn': str(self.name), 'td': str(self.description), 'ts':str(self.size), 'tc': str(self.created_at), 'tp': str(self.project.id_project), 'tu': str(self.user.id_user)}
        sql = "INSERT INTO scrum_task (name, description, size, created_at, project_id, user_id) VALUES ('%(tn)s', '%(td)s', '%(ts)s', '%(tc)s', '%(tp)s', '%(tu)s')" % args
        c.execute(sql)
        c.close()
        conn.close() 

class Comment(models.Model):
    id_comment = models.AutoField(primary_key=True)
    body = models.TextField(max_length=500, verbose_name='Текст комментария')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='CommentTask')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='CommentUser')

    def __str__(self):
        return self.body
    
    def GetAllTaskComments(self):
        conn = sqlite3.connect('scrum.sqlite3')
        c = conn.cursor()
        sql = 'SELECT * FROM scrum_task WHERE task_id = %s' % str(self.task)       
        c.execute(sql)
        comment = c.fetchall()
        c.close()
        conn.close()
        return comment

    def InsertComment(self):        
        conn = sqlite3.connect('scrum.sqlite3')
        c = conn.cursor()
        args = {'cb': str(self.body), 'ct': self.task, 'cu': self.user}
        sql = 'INSERT INTO scrum_comment (body, ) VALUES %(cb)s %(ct)s %(cu)s' % args
        c.execute(sql)
        c.close()
        conn.close() 
    
    