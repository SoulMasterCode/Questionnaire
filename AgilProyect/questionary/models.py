#Models
from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

# Create your models here.
class Questionnaire(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    questionnaire = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.questionnaire

class Section(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    section = models.CharField(max_length=45)

    def __str__(self):
        return self.section

class Question(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.answer

    

    # users = [{
    #             'first_name':'David',
    #             'last_name':'Rodriguez Canto',
    #             'passwd':'12345',
    #             'email':'david_rod@gmail.com',
    #             'user_type_id':1
    #         },
    #         {
    #             'first_name':'Pascual',
    #             'last_name':'Gonsalez Rodriguez',
    #             'passwd':'54321',
    #             'email':'pascualgonzales@gmail.com',
    #             'user_type_id':1
    #         },
    #         {
    #             'first_name':'Edwin',
    #             'last_name':'Baeza Suaste',
    #             'passwd':'789010',
    #             'email':'edwinbz@gmail.com',
    #             'user_type_id':1}
    #         ]