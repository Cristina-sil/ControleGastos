import datetime

from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import TransacaoForm
from .models import Transacao


def home (request):
    transacao = Transacao.objects.all()
    return render(request, 'contas/home.html',context={
        'transacao': transacao,    
    })

def cadastrarTransacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_home')
    data['form'] = form
    return render(request, 'contas/form.html',data)




