from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .views import *

class reg_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class task_form(ModelForm):
    deadline = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    #user = forms.ModelMultipleChoiceField(queryset=beneficiare.objects.filter(user__id=1))

    # def __init__(self, user, *args, **kwargs):
    #     super(task_form, self).__init__(*args, **kwargs)
    #     self.fields['user'].queryset = User.objects.filter(pk=user.id)
    class Meta:
        model = tasks
        fields = '__all__'
        exclude = ['user']


class settigs_form(ModelForm):
    class Meta:
        model = beneficiare
        fields='__all__'