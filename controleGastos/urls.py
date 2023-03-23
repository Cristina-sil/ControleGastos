
from contas.views import cadastrarTransacao, home, update
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='url_home'),
    path('nova/',cadastrarTransacao,name='Nova_Transacao'),
    path('update/<int:pk>',update,name = 'url_update'),
]

