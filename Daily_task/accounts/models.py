from django.db import models
from datetime import timedelta, datetime
# Create your models here.

class tasks(models.Model):
    category = (
        ('highest','higest'),
        ('medium','medium'),
        ('low','low')
    )
    date_created = models.DateTimeField(auto_now_add=True)
    days_to_do = models.IntegerField(blank=True,)
    deadline = models.DateTimeField(default=datetime.now()+timedelta(days=days_to_do))
    description = models.TextField(blank=True)
    title = models.CharField(blank=False)
    is_complete = models.BooleanField(default=False, blank=False)
    completed_on_time  = models.BooleanField(default=False, blank=False)
    priority = models.CharField(choices=category)



