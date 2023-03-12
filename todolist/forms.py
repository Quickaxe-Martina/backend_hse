from django import forms
from .models import TodoModel


choices = [(1, 'Низкий'), (2, 'Средний'), (3, 'Высокий')]

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