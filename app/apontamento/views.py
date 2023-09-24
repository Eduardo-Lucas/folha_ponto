from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def apontamento_list(request, login_url="users:login"):
    return render(request, "apontamento/apontamento-list.html", {})
