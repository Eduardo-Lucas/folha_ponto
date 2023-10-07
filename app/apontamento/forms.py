from apontamento.models import Ponto
from django import forms

class FolhaPontoForm(forms.ModelForm):
        
    class Meta:
        model = Ponto 
        fields = ("usuario_id", "entrada", "saida")

