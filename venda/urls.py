from django.urls import path
from .views import venda

urlpatterns = [
    path('cadastro/', venda, name="venda")
]
