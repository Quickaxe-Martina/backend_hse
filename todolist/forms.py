from django import forms
from .models import TodoModel


choices = [(1, 'Высокий'), (2, 'Средний'), (3, 'Низкий')]

class TodoForm(forms.ModelForm):
    priority = forms.ChoiceField(
        choices=choices
    )
    class Meta:
        model = TodoModel
        fields = (
            'name',
            'description',
            'is_done'
        )
        widgets = {
            'name': forms.TextInput,
            'description': forms.Textarea,
            'is_done': forms.CheckboxInput
        }