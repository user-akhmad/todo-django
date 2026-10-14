from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description"]

        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Что нужно сделать"}),
            "description": forms.Textarea(attrs={"placeholder": "Детали(необязательно)", "rows": 3}),
        }