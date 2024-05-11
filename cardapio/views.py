from django.shortcuts import render
from .models import Produto

# Create your views here.
def home(request):
    return render(request, 'home.html')

def itensCarrinho(request):
    return render(request, 'itensCarrinho.html')

def localEntrega(request):
    return render(request, 'localEntrega.html')

def resumoCarrinho(request):
    return render(request, 'resumoCarrinho.html')

def lista_produtos(request, ID_Categoria=None):
    if ID_Categoria:
        produtos = Produto.objects.filter(ID_Categoria=ID_Categoria)  # Filtra produtos por categoria
    else:
        produtos = Produto.objects.all()  # Busca todos os produtos se nenhum ID de categoria for fornecido
    return render(request, 'home.html', {'produtos': produtos})


def produto_card_view(request, categoria):
    produtos = Produto.objects.filter(categoria=categoria).all()
    return render(request, 'produto_list.html', {'produtos': produtos })