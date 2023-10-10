from django import forms
from django.contrib.auth.models import User
from apontamento.models import Ponto


class DateInput(forms.DateInput):
    input_type = "date"


class FolhaPontoForm(forms.Form):
    usuario = forms.ModelChoiceField(queryset=User.objects.all().order_by("username"))
    entrada = forms.DateField(widget=DateInput)
    saida = forms.DateField(widget=DateInput)
