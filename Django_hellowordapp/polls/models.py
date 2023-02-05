import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model): #hereda de models
    """
        Model for Question table in db
    """
    question_text=models.CharField(max_length=200) #contiene las preguntas
    pub_date=models.DateTimeField('Date published')
    
    def __str__(self) -> str:
        """
            Cuando se solicita el str de la clase, devuelve el texto de la pregunta y no Question.objectType()
        """
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    """
        Model for Choice table in db
    """
    question=models.ForeignKey(to=Question, # usa de llave foranea el id de la Question
                               on_delete=models.CASCADE, # Cuando se elimina una Question tambien se eliminan las choices relacionadas
                               )
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    
    def __str__(self) -> str:
        """
            Cuando se solicita el str de la clase, devuelve el texto de la repuesta y no Choice.objectType()
        """
        return self.choice_text
    
