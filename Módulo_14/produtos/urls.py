from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_produtos, name='listar_produtos'),
    path('criar/', views.criar_produto, name='criar_produto'),
    path('atualizar/<int:id>/', views.atualizar_produto, name='atualizar_produto'),
    path('excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),
]
