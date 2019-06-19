from django.shortcuts import render, redirect
from django.http import HttpResponse

#Django
from datetime import datetime  
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

#models
from .models import *

#Forms
from .forms import *

class DetailQuestView(DetailView, LoginRequiredMixin):
    model = Questionnaire
    template_name= 'questionary/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        questionnaire = self.get_object()
        questions = list()
        answers = list()

        context['sections'] = Section.objects.filter(questionnaire=questionnaire.pk)
        sections = context['sections']

        for section in sections:
            questions.append(Question.objects.filter(section=section))
        context['questions'] = questions

        for question_query in questions:
            for question in question_query:
                answers.append(Answer.objects.filter(question=question))
        print(answers)
        context['answers'] = answers
        return context



# Create your views here.
@login_required
def dictionary(request):
    
    return render(request, 'questionary/feed.html', {'posts':'posts'})

'''    data = []
    for item in questions:
        data.append(
            """
            <table style="margin:auto">
                <tr>
                    <th>#</th>
                    <th>Pregunta</th>
                    <th>Respuesta</th>
                </tr>
                <tr>
                    <td>{id}</td>
                    <td>{question}</td>
                    <td>{answers}</td>
                </tr>
            </table>

            """.format(**item)
        )'''

# @login_required
# def CreateQuestionnaire(request):
#     if request.method == "POST":
#         form = QuestionnaireForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("questionary:questionnaires")
#     else:
#         form = QuestionnaireForm()
#     return render(request, 'questionary/new.html', {'form': form, 'user': request.user, 'profile':request.user.profile})

class CreateQuestionnaireView(CreateView, LoginRequiredMixin):
    template_name = "questionary/new.html"
    form_class = QuestionnaireForm
    success_url = reverse_lazy('questionary:questionnaires')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile

        return context


class Questionnaire_View(ListView, LoginRequiredMixin):
    model = Questionnaire
    template_name= 'questionary/questionnaire.html'
    paginate_by = 2
    context_object_name = 'posts'
    queryset = Questionnaire.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sections'] =  Section.objects.all()
        context['ques'] =  Question.objects.all()
        context['ans'] =  Answer.objects.all()

        return context

# @login_required
# def Questionnaire_View(request):
#     quests = Questionnaire.objects.all()
#     secs = Section.objects.all()
#     question = Question.objects.all()
#     answer = Answer.objects.all()
#     return render(request, 'questionary/questionnaire.html', {  'posts':quests,
#                                                                 'sections':secs,
#                                                                 'ques':question,
#                                                                 'ans':answer, })


# @login_required
# def QuestionnaireData_View(request):
#     return render(request, 'questionary/questionnaire_data.html')
    

# def usuarios(request):
#     users = User.objects.all()
#     dic_user = []
#     for user in users:
#         dic_user.append({
#             'nombre':user.first_name,
#             'apellido':user.last_name,
#             'correo':user.email,
#             'tipo_usuario':user.user_type
#         })

#     return render(request, 'users.html', {'users':dic_user})
