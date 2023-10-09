from django import forms
from apontamento.models import Ponto


class DateInput(forms.DateInput):
    input_type = "date"
    format = "dd/MM/yyyy"


class FolhaPontoForm(forms.ModelForm):
    class Meta:
        model = Ponto
        fields = ("usuario_id", "entrada", "saida")

        widgets = {
            "entrada": forms.DateInput(),
            "saida": forms.DateInput(),
        }
