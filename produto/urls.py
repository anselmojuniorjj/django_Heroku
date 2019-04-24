from django.urls import path
from .views import cad_produto


urlpatterns = [
    path('cadastro/', cad_produto, name="produto")
]