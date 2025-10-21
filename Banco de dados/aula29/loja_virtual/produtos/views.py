from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse
from .models import Produto
import json

# Listar todos os produtos
def listar_produtos(request):
    produtos = list(Produto.objects.values())
    return JsonResponse(produtos, safe=False)

# Criar um produto via POST
def criar_produto(request):
    if request.method == "POST":
        data = json.loads(request.body)
        produto = Produto.objects.create(
            nome=data['nome'],
            preco=data['preco'],
            estoque=data['estoque']
        )
        return JsonResponse({'id': produto.id, 'nome': produto.nome})
    return HttpResponse("Use POST para criar produtos", status=400)

# Atualizar produto via PUT
def atualizar_produto(request, produto_id):
    if request.method == "PUT":
        try:
            produto = Produto.objects.get(id=produto_id)
            data = json.loads(request.body)
            produto.nome = data.get('nome', produto.nome)
            produto.preco = data.get('preco', produto.preco)
            produto.estoque = data.get('estoque', produto.estoque)
            produto.save()
            return JsonResponse({'id': produto.id, 'nome': produto.nome})
        except Produto.DoesNotExist:
            return HttpResponse("Produto não encontrado", status=404)
    return HttpResponse("Use PUT para atualizar produtos", status=400)

# Deletar produto via DELETE
def deletar_produto(request, produto_id):
    if request.method == "DELETE":
        try:
            produto = Produto.objects.get(id=produto_id)
            produto.delete()
            return JsonResponse({'mensagem': 'Produto deletado'})
        except Produto.DoesNotExist:
            return HttpResponse("Produto não encontrado", status=404)
    return HttpResponse("Use DELETE para deletar produtos", status=400)
