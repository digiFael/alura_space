

from django.contrib import admin
from django.urls import path,include


# eu crio um path para quando chegar uma requisiaçao no endereço principal eu quero que a funçao view seja chamada   
urlpatterns = [
    path("admin/", admin.site.urls),
    # aqui eu estou colocando a inicializaçao que começava atravex do index agora ele esta ligado a galeria e incluir a urls
    path("",include('galeria.urls'))
]
