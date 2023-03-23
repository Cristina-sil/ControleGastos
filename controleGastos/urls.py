
from django.contrib import admin
from django.urls import path

from contas.views import cadastrarTransacao, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nova/',cadastrarTransacao,name='Nova_Transacao'),
    path('',home,name='url.home'),
]

