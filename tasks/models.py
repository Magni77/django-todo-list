from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class TaskModel(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=300)
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def get_absolute_url(self):
        return reverse("tasks:detail", kwargs={"id": self.id})

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title