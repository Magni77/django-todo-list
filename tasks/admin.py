from django.contrib import admin
from .models import TaskModel

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
   list_display = ['title']
   ordering = ['title']

   class Meta:
       model = TaskModel

admin.site.register(TaskModel, TaskAdmin)
