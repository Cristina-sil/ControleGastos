import datetime

from django.http import HttpResponse
from django.shortcuts import render

from .models import Transacao

# Create your views here.

def home (request):
    transacao = Transacao.objects.all()
    return render(request, 'contas/home.html',context={
        'transacao': transacao,    
    })

