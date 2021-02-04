from django.contrib import admin
from .models import Task_record,Task,Task_type

admin.site.register(Task_record)
admin.site.register(Task)
admin.site.register(Task_type)