from django.shortcuts import render


def apontamento_list(request):
    return render(request, "apontamento/apontamento-list.html", {})
