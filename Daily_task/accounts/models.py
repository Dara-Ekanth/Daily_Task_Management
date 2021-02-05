from django.db import models
from datetime import timedelta, datetime
from django.core.validators import RegexValidator

# Create your models here.

class tasks(models.Model):
    category = (
        ('highest','higest'),
        ('medium','medium'),
        ('low','low')
    )

    # def deadline_cal(self):
    #     return datetime.now()+ timedelta(days=self.days_to_do)

    date_created = models.DateTimeField(auto_now_add=True)
    days_to_do = models.IntegerField(blank=True,)
    #deadline = models.DateTimeField(default=deadline_cal())
    #deadline = models.DateTimeField(default=lambda: datetime.now()+timedelta(days=30))
    deadline = models.DateField(max_length=8,blank=True,default=1)
    description = models.TextField(blank=True)
    title = models.CharField(primary_key=True,blank=False, max_length=100)
    is_complete = models.BooleanField(default=False, blank=False)
    completed_on_time  = models.BooleanField(default=False, blank=False)
    priority = models.CharField(choices=category, max_length=32)


    def __str__(self):
        return str(self.title)

class benificiary(models.Model):
    name = models.CharField(primary_key=True, max_length=32)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    email_id = models.EmailField(max_length=100,unique=True,blank=True)
    def __str__(self):
        return str(self.name)




