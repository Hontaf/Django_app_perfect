from django.urls import path
from .views import CategoryView


#Mes routes :
urlpatterns = [
    path("",CategoryView.as_view(),name="book"),
]