from django.forms import ModelForm

from .models import Categoria, Transacao


class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['nome','data_transacao','descricao','valor',
                  'observacoes','Categoria']

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
