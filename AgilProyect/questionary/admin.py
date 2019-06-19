# Django
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#My Models on Questionary
from .models import *

# Register your models here.
class SectionInline(admin.StackedInline):
    model = Section
    can_delete = False
    verbose_name_plural = 'Sections'

class QuestionnaireAdmin(admin.ModelAdmin):
    inlines = (SectionInline,) #Para Agregar el formulario de las pregunatas al formulario de seccion
    list_display = ('pk', 'user', 'questionnaire')
    list_display_links = ('pk','user',)
    list_editable = ('questionnaire',)
    search_fields = ('questionnaire', 'pk', 'user__username')
    list_filter = ('created', 'modified')

    readonly_fields = ('created', 'modified')

class QuestionInline(admin.StackedInline):
    model = Question
    can_delete = False
    verbose_name_plural = 'Questions'

class SectionAdmin(admin.ModelAdmin):
    inlines = (QuestionInline,)
    list_display = ('pk', 'questionnaire', 'section')
    list_display_links = ('pk',)
    list_editable = ('section',)
    search_fields = ('section', 'pk', 'Questionnaire__questionnaire')

class AnswerInline(admin.StackedInline):
    model = Answer
    can_delete = False
    verbose_name_plural = 'Answers'

class QuestionoAdmin(admin.ModelAdmin):
    inlines = (AnswerInline,)
    list_display = ('pk', 'section', 'question')
    list_display_links = ('pk',)
    list_editable = ('question',)
    search_fields = ('question', 'pk', 'Section__section')

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'question', 'answer')
    list_display_links = ('pk',)
    list_editable = ('answer',)
    search_fields = ('answer', 'pk', 'Question__question')

admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Question, QuestionoAdmin)
admin.site.register(Answer, AnswerAdmin)
