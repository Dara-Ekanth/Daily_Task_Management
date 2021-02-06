from .models import *
from django import forms
from django.forms import ModelForm

class reg_form(forms.ModelForm):
    class Meta:
        model = benificiary
        fields = '__all__'

class task_form(forms.ModelForm):
    class Meta:
        model = tasks
        fields = '__all__'