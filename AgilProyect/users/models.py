#django
from django.db import models
from django.contrib.auth.models import User

#Questionary Models
# from questionary.models import *

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    phone_number = models.CharField(max_length=20, blank=True)
    picture = models.ImageField(upload_to='users/Pictures', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        #regresa el username
        return self.user.username

# class Chosen_Answer(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)