from django.urls import path
from .views import home, my_logout
#from .views import Home3
# from django.views.generic import TemplateView

urlpatterns = [
    path('', home, name="home"),
    path('logout', my_logout, name="logout")
    # path('home2/', TemplateView.as_view(template_name="home2.html")),
    # path('home3/', Home3.as_view(template_name="home3.html"))
]