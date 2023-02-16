from django.shortcuts import render #conecta la view con el template
from django.shortcuts import get_object_or_404 ,get_list_or_404 #genera un proceso Question.objects.get(), que al incumplir retorna 404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
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
    question = get_object_or_404(Question, pk=question_id)
    return render(
        request, "polls/results.html", {
            "question":question
        }
    )
def vote(request, question_id)->HttpResponse:
    """
        Muestra que pregunta esta votando.
        
        Parameters
        ---
            request: 
            question_id: primary key of Quetion objects
    """
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    
    except (KeyError, Choice.DoesNotExist):
        return render(request,"polls/detail.html",{
            "question":question,
            "error_message":"No elegiste una repuesta"
        })
        
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id)))

