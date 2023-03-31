import datetime
from urllib import request

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CategoriaForm, TransacaoForm
from .models import Categoria, Transacao


def home (request):
    transacao = Transacao.objects.all()
    return render(request, 'contas/home.html',context={
        'transacao': transacao,    
    })

def principalCategorias(request):
    categoria = Categoria.objects.all()
    return render(request,'contas/categorias.html',context={
        'categoria' : categoria
    } )

def cadastrarTransacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_home')
    data['form'] = form
    return render(request, 'contas/form.html',data)

def cadastrarCategoria(request):
    data = {}
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_categorias')
    data['form'] = form
    return render(request,'contas/formCategoria.html',data)
  
def update(request,pk):
    data = {}
    transacao = get_object_or_404(Transacao, pk=pk) #Retorna o 404 caso não exista registro com o id passado
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_home')
    
    data['form'] = form 
    data['transacao'] = transacao
    return render(request, 'contas/form.html',data)

def atualizarCategoria(request,pk):
    data = {}
    categoria = Categoria.objects.get(pk=pk)
    form = CategoriaForm(request.POST or None, instance=categoria)
    if form.is_valid():
        form.save()
        return redirect('url_categorias')
    
    data['form'] = form
    data['categoria'] = categoria
    return render(request,'contas/formCategoria.html',data)


def delete(request,pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_home')

def deleteCategoria(request,pk):
    categoria = Categoria.objects.get(pk=pk)
    categoria.delete()
    return redirect('url_categorias')






