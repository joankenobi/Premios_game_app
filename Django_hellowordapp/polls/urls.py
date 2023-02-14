from django.urls import path
from . import views

app_name="polls" #define la subraiz de la url, lo lee internamente Django.

urlpatterns=[
    path(route="",
         view=views.index,
         name="index"), # se aplica lo descrito en urls.py de la app principal
    path(route="<int:question_id>/", #<> indica el parametro que le va a llegar a la view funtion
         view=views.detail,
         name="detail" #etiqueta URL dinamica para Django
         ), 
    path(route="<int:question_id>/results/",
         view=views.results,
         name="results"),
    path(route="<int:question_id>/vote/",
         view=views.vote,
         name="vote")
]

