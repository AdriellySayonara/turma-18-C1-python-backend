from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.listar_produtos),
    path('produtos/criar/', views.criar_produto),
    path('produtos/atualizar/<int:produto_id>/', views.atualizar_produto),
    path('produtos/deletar/<int:produto_id>/', views.deletar_produto),
]
