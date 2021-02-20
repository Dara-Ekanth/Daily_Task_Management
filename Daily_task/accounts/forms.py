from .models import *
from django.forms import ModelForm

class reg_form(ModelForm):

    class Meta:
        model = beneficiare
        fields = '__all__'

class task_form(ModelForm):
    class Meta:
        model = tasks
        fields = '__all__'