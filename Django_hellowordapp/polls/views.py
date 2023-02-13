from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request): #la vista principal casi siempre es nombrada Index (buenas practicas)
    "Muestra la pagina principal"
    return HttpResponse("Hola estas en la pagina principal de peliculas questions")

def detail(request, question_id)->HttpResponse:
    """
        Muestra las diferentes preguntas y opciones para votar.
        
        Parameters
        ---
            request: 
            question_id: primary key of Quetion objects
    """
    return HttpResponse(f"You are viewing the question number{question_id}")

def results(request, question_id)->HttpResponse:
    """
        Muestra los resultados de la votacion.
        
        Parameters
        ---
            request: 
            question_id: primary key of Quetion objects
    """
    return HttpResponse(f"You are viewing the results of question number{question_id}")

def vote(request, question_id)->HttpResponse:
    """
        Muestra que pregunta esta votando.
        
        Parameters
        ---
            request: 
            question_id: primary key of Quetion objects
    """
    return HttpResponse(f"You are voting to question number{question_id}")

