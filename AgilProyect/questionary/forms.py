#Forms
from django.forms  import ModelForm

# Models
from questionary.models import *

class QuestionnaireForm(ModelForm):
    class Meta:
        model = Questionnaire
        fields = ("user","profile","questionnaire")