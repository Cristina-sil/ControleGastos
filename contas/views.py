import datetime
from urllib import request

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

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

def update(request,pk):
    data = {}
    transacao = get_object_or_404(Transacao, pk=pk) #Retorna o 404 caso não exista registro com o id passado
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_home')
    
    data['form'] = form 
    return render(request, 'contas/form.html',data)





