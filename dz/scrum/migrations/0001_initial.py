# Generated by Django 3.1.3 on 2021-01-17 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id_project', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Название проекта')),
                ('description', models.TextField(max_length=1024, verbose_name='Описание проекта')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='Название задачи')),
                ('password', models.CharField(max_length=10, verbose_name='Пароль')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id_task', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Название задачи')),
                ('description', models.TextField(max_length=1024, verbose_name='Описание задачи')),
                ('size', models.IntegerField(verbose_name='Размер задачи')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TaskProject', to='scrum.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TaskUser', to='scrum.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id_comment', models.AutoField(primary_key=True, serialize=False)),
                ('body', models.TextField(max_length=500, verbose_name='Текст комментария')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CommentTask', to='scrum.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CommentUser', to='scrum.user')),
            ],
        ),
    ]
