from django.urls import path
from portal import views

urlpatterns = [
    path('', views.home, name='home'),
    path('retorno/', views.TesteRetorno, name='retorno'),
    path('avaliacao', views.filtraCondominio, name='avaliacao'),
    path('referenciais/', views.referenciais, name='referenciais'),
    path('calculos/', views.calcula, name='calcular'),
    path('imoveis/', views.imovel, name='imoveis'),
    path('imovel/add/', views.imovel_add, name='imovel_add'),
    path('imovel/edit/<int:imovel_pk>/', views.imovel_edit, name='editar'),
    path('imovel/delete/<int:imovel_pk>/', views.imovel_delete, name='imovel_delete'),
    path('estadoConservacao/', views.estadoConserv, name='estadoConservacao'),
    path('estadoConserv/add', views.estadoConserv_add, name='estadoConserv_add'),
    path('condominio/', views.condominio, name='condominio'),
    path('cond/add', views.cond_add, name='cond_add'),
    path('cond/edit/<int:cond_pk>/', views.cond_edit, name='cond_edit'),
    path('cond/delete/<int:cond_pk>/', views.cond_delete, name='cond_delete'),
    path('tipo/', views.tipo, name='tipo'),
    path('tipo/add', views.tipo_add, name='tipo_add'),
    path('padrao/', views.padrao, name='padrao'),
    path('padrao/add', views.padrao_add, name='padrao_add'),

]
