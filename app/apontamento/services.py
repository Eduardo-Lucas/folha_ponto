from django.db.models import Q
from apontamento.models import Ponto


class PontoService:
    def ponto_list(self, usuario_id, data_inicial, data_final):
        data_query = Q(
            Q(
                data_entrada__gte=data_inicial,
            )
            & Q(
                data_saida__lte=data_final,
            )
        )
        query = Ponto.objects.all()

        return query
