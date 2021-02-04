from django import forms
from .models import Todo
from django.forms import ModelForm

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'