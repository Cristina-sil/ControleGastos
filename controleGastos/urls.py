
from contas.views import (cadastrarCategoria, cadastrarTransacao, delete, home,
                          principalCategorias, update)
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='url_home'),
    path('nova/',cadastrarTransacao,name='Nova_Transacao'),
    path('update/<int:pk>',update,name = 'url_update'),
    path('delete/<int:pk>',delete, name='url_delete'),
    path('categorias/',principalCategorias,name= 'url_categorias'),
    path('cadastrarCategoria',cadastrarCategoria,name='url_novaCategoria'),
]

