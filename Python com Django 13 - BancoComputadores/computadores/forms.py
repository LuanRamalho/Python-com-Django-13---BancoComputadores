from django import forms
from .models import Computador

class ComputadorForm(forms.ModelForm):
    class Meta:
        model = Computador
        fields = '__all__'
