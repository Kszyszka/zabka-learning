from django.db import models
from django.db.models.signals import post_init
from quizAPP.models import *

# Create your models here.

class TestAttempt(models.Model):

    taken_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    taken_by_name = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    correct_key = models.CharField(max_length=200)  #this will be a string of corrent answers, for example '14124341312'
    given_key = models.CharField(max_length=200)    #this will be a string of answers given by the user, for example '123141323'
    score_out_of = models.CharField(max_length=200)      # 'recieved/max'
    score_percent = models.FloatField(max_length=200)   #what score did the user get
    passed = models.BooleanField()                  #did he pass?


    def get_score(self):
        got,max = self.score_out_of.split('/')
        return (int(got),int(max))
    
    def process(self):
        
        max = len(list(self.correct_key))
        got = 0
        for i in range(max):
            if self.correct_key[i] == self.given_key[i]:
                got += 1

        self.score_out_of = f'{got}/{max}'
        self.score_percent = (got / max) * 100
        self.passed = True if self.score_percent >= 50 else False
    
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)   #calling the constructor of parent class first

        try:
            self.process()
        except Exception as e:
            pass

        

        


        
