# Rutas del Cuestionario

# Django
from django.urls import path

# views
from questionary.views import *

# # Templates
# from django.views.generic import TemplateView

urlpatterns = [
    path('', Questionnaire_View.as_view(), name='questionnaires'),
    path('<slug:pk>/', DetailQuestView.as_view(), name = 'detail'),
    path('new', CreateQuestionnaireView.as_view(), name='new'),
]