from django.urls import path
#from .views import list_person
# from .views import add_person
# from .views import update_person
# from .views import delete_person
from .views import PersonList
from .views import PersonDetail
from .views import PersonCreate
from .views import PersonUpdate
from .views import PersonDelete

urlpatterns = [
    #path('list/', list_person, name="list_person"),
    # path('new/', add_person, name="add_person"),
    # path('update/<int:pk>/', update_person, name="update_person"),
    # path('delete/<int:pk>', delete_person, name="delete_person"),
    path('person_list/', PersonList.as_view(), name="person_list"),
    path('person_detail/<int:pk>/', PersonDetail.as_view(), name="person_detail"),
    path('person_create/', PersonCreate.as_view(), name="person_create"),
    path('person_update/<int:pk>', PersonUpdate.as_view(), name="person_update"),
    path('person_delete/<int:pk>', PersonDelete.as_view(), name="person_delete")
]
