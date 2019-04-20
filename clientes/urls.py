from django.urls import path
from .views import list_person
from .views import add_person
from .views import update_person
from .views import delete_person

urlpatterns = [
    path('list/', list_person, name="list_person"),
    path('new/', add_person, name="add_person"),
    path('update/<int:pk>/', update_person, name="update_person"),
    path('delete/<int:pk>', delete_person, name="delete_person")
]
