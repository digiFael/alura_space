from django.shortcuts import render


def index(request): #quando chegar uma requisao para index mostra esse httpResponse
    return render(request,'galeria/index.html') # eu sempre coloco o paramtero request e depois eu coloco onde o nome do html , o arquivo que eu quero colocar 

def imagem(request):
    return render(request, 'galeria/imagem.html')