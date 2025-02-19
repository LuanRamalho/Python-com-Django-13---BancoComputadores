from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_computadores, name='lista_computadores'),
    path('adicionar/', views.adicionar_computador, name='adicionar_computador'),
    path('editar/<int:id>/', views.editar_computador, name='editar_computador'),
    path('excluir/<int:id>/', views.excluir_computador, name='excluir_computador'),
]
