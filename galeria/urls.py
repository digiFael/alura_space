from django.urls import path
from galeria.views import index, imagem

#criar uma lista para manter os endereços relacionados a galeria 

urlpatterns = [
    
    path('',index),
    path('imagem/', imagem, name='imagem'),
]
