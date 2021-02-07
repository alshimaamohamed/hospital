# Generated by Django 3.1.2 on 2021-02-06 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Person', '0001_initial'),
        ('Items', '0002_auto_20210206_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
                ('name', models.CharField(max_length=300, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task_record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task_name', models.CharField(max_length=300, unique=True)),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('queued', 'queued'), ('running', 'running'), ('done', 'done'), ('failed', 'failed'), ('rejected', 'rejected')], max_length=32)),
                ('arg1', models.CharField(max_length=50, null=True)),
                ('arg2', models.CharField(max_length=50, null=True)),
                ('arg3', models.CharField(max_length=50, null=True)),
                ('arg4', models.CharField(max_length=50, null=True)),
                ('arg5', models.CharField(max_length=50, null=True)),
                ('arg6', models.CharField(max_length=50, null=True)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Person.person')),
                ('robot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Items.robot')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
                ('task_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tasks.task_type')),
            ],
        ),
    ]
