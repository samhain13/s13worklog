from django import forms

from .models import Category
from .models import LogItem
from .models import Task


class CategoryForm(forms.ModelForm):
    class Meta:
        fields = ['name', 'description']
        model = Category


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class LogItemForm(forms.ModelForm):
    class Meta:
        fields = ['task', 'start_dt', 'end_dt', 'notes']
        model = LogItem


class TaskForm(forms.ModelForm):
    class Meta:
        fields = ['name', 'description', 'done']
        model = Task
