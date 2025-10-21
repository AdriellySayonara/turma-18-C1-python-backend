from django.http import JsonResponse

def home(request):
    return JsonResponse({"mensagem": "Bem-vindo à API da Loja Virtual"})
