from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apontamento.services import PontoService


@login_required
def apontamento_list(request, login_url="users:login"):
    return render(request, "apontamento/apontamento-list.html", {})


def folha_ponto(request):
    data_inicial = "2023-09-01"
    data_final = "2023-09-30"

    service = PontoService()

    pontos = service.ponto_list(data_inicial, data_final)

    return render(request, "apontamento/folha-ponto.html", {"pontos": pontos})
