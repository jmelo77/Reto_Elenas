from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from elenas_apps.base.models import BaseMixin

# Create your models here.
class Task(BaseMixin):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=600, null=False)
    completed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('updated_at',)

