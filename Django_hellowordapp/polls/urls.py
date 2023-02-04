from django.urls import path
from . import views

urlpatterns=[
    path(route="",
         view=views.index,
         name="index") # se aplica lo descrito en urls.py de la app principal
]