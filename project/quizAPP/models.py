from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    #identifier = models.CharField(max_length=20)    #instead of ID, bcs its a builtin keyword
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='quizzes')
    #threshold = models.IntegerField
    
    def __str__(self):
        return self.title
    
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)

    question_text = models.CharField(max_length=500)
    answer1 = models.CharField(max_length=200)
    answer2 = models.CharField(max_length=200)
    answer3 = models.CharField(max_length=200)
    answer4 = models.CharField(max_length=200)
    correct_answer = models.IntegerField()      #choice from 1 to 4

    def __str__(self):
        return self.question_text
    
    



