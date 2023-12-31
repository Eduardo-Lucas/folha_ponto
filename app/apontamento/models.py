from django.db import models
from django.contrib.auth.models import User


class Ponto(models.Model):
    id = models.IntegerField(
        primary_key=True,
    )
    entrada = models.DateTimeField()
    primeiro = models.BooleanField(default=False)
    segundo = models.BooleanField(default=False)
    atraso = models.BooleanField(default=False)
    saida = models.DateTimeField(null=True, blank=True)
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    fechado = models.BooleanField(default=False)
    cliente_id = models.IntegerField(null=True, blank=True)
    tiporeceita_id = models.IntegerField(null=True, blank=True)
    atrasoautorizado = models.BooleanField(default=False)

    class Meta:
        ordering = ("entrada",)

    
    @property
    def difference(self):
        if self.saida is not None:
            return self.saida - self.entrada
        return 0
        
    def __str__(self) -> str:
        return f"{self.usuario_id} {self.entrada} {self.saida} {self.difference}"
