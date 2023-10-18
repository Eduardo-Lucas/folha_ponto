from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from apontamento.services import PontoService
from apontamento.forms import FolhaPontoForm
from apontamento.models import Ponto


@login_required
def apontamento_list(request, login_url="users:login"):
    return render(request, "apontamento/apontamento-list.html", {})


def folha_ponto(request):
    form = FolhaPontoForm(request.POST or None)
    context = {"pontos": [], "form": form, "nome": ""}
    if request.method == "POST":
        usuario = User.objects.filter(username=form["usuario"]).first()
        service = PontoService()
        pontos = service.ponto_list(usuario.id, form["entrada"], form["saida"])

        nome = usuario.username
        context = {"pontos": pontos, "form": form, "nome": nome}

    else:
        form = FolhaPontoForm()

    return render(
        request,
        "apontamento/folha-ponto.html",
        context,
    )
