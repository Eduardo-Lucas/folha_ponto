from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from apontamento.services import PontoService


@login_required
def apontamento_list(request, login_url="users:login"):
    return render(request, "apontamento/apontamento-list.html", {})


def folha_ponto(request):
    usuario_id = 6
    data_inicial = "2023-09-01"
    data_final = "2023-09-30"

    service = PontoService()

    usuario = User.objects.get(id=usuario_id)
    nome = usuario.username

    pontos = service.ponto_list(usuario_id, data_inicial, data_final)

    return render(
        request,
        "apontamento/folha-ponto.html",
        {"pontos": pontos, "nome": nome},
    )
