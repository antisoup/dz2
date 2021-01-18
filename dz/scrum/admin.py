from django.contrib import admin
from .models import Project, Task, User, Comment

@admin.register(Project, Task, User, Comment)
class DefaultAdmin(admin.ModelAdmin):
    pass
