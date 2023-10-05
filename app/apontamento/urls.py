from django.urls import path
from .views import *

app_name = "apontamento"

urlpatterns = [
    path("", apontamento_list, name="apontamento_list"),
    path("folha-ponto", folha_ponto, name="folha-ponto"),
]
