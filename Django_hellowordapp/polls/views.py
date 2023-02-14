from django.shortcuts import render #conecta la view con el template
from django.shortcuts import get_object_or_404 ,get_list_or_404 #genera un proceso Question.objects.get(), que al incumplir retorna 404
from django.http import HttpResponse
from .models import Question, Choice
# Create your views here.

def index(request)->HttpResponse: #la vista principal casi siempre es nombrada Index (buenas practicas)
    """Muestra la pagina principal"""
    latest_question_list=Question.objects.all()
    return render(request=request,
                  template_name="polls/index.html", #se juntan todo el contenido de las carpetas templates y se escoge la carpeta polls.
                  context={
                      "latest_question_list":latest_question_list
                  })

def detail(request, question_id)->HttpResponse:
    """
        Muestra las diferentes preguntas y opciones para votar.
        
        Parameters
        ---
            request: request
            question_id: primary key of Quetion objects
    """
    question=get_object_or_404(Question, pk=question_id)
    return render(request=request, template_name="polls/detail.html",context={
        "question":question
    })

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

