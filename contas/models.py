from django.db import models


class Categoria (models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Transacao(models.Model):
    nome = models.CharField(max_length=25)
    data_transacao = models.DateTimeField(auto_now_add=False)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    observacoes = models.TextField(null = True, blank=True)
    Categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)

    def __str__(self):
        return self.nome
