from django import forms
from .models import ToDo

class AddToDo(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = '__all__'
        widgets = {
            'todo': forms.TextInput(attrs={'autocomplete': 'off'}),
        }