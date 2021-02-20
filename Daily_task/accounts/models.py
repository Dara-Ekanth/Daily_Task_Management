from django.db import models
from datetime import timedelta, datetime
from django.core.validators import RegexValidator
from django.conf import settings


# Create your models here


class beneficiare(models.Model):
    name = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null = True)  # validators should be a list
    email_id = models.EmailField(max_length=100,unique=True,blank=True, null=True)

    def __str__(self):
        return str(self.name)

class tasks(models.Model):

    category = (
        ('highest','higest'),
        ('medium','medium'),
        ('low','low'),
    )

    # def deadline_cal(self):
    #     return datetime.now()+ timedelta(days=self.days_to_do)
    title = models.CharField(max_length=100,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    days_to_do = models.IntegerField()
    #deadline = models.DateTimeField(default=deadline_cal())
    #deadline = models.DateTimeField(default=lambda: datetime.now()+timedelta(days=30))
    deadline = models.DateField(auto_now=True)
    description = models.TextField(blank=False)
    is_complete = models.BooleanField(default=False, null=True)
    completed_on_time  = models.BooleanField(default=False, null=True)
    priority = models.CharField(choices=category, max_length=32)
    user = models.ForeignKey(beneficiare,null=True,blank=True,on_delete=models.SET_NULL)


    def __str__(self):
        return str(self.title)






