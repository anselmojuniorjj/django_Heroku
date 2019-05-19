from django.shortcuts import render, redirect
from django.contrib.auth import logout
# from django.views.generic import TemplateView

# Create your views here.

def home(request):
    return render(request, 'home.html')

# TODO : TESTES
def my_logout(request):
    logout(request)
    return redirect(home)

# class Home3(TemplateView):
#     template_name = 'home3.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['minha_variavel'] = 'Hello Class based view'
#         return context