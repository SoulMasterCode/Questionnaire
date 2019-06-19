#django
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#models
from users.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('pk', 'user', 'phone_number', 'picture',)
    list_display_links = ('pk','user',)
    list_editable = ('phone_number', 'picture',)
    search_fields = ('user__username', 'user__email', 'phone_number','pk','user__first_name', 'user__last_name',)
    list_filter = ('user__is_active','user__is_staff','created', 'modified',)

    fieldsets = (('Perfil',{
        'fields':(('user','picture',),),
    }),
    ('Datos extra',{
        'fields':('phone_number','created','modified',),
    }),)

    readonly_fields = ('created', 'modified')

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

# class QuestionInline(admin.StackedInline):
#     model = Question
#     can_delete = False
#     verbose_name_plural = 'Questions'

# # @admin.register(Section)
# class SectionAdmin(admin.ModelAdmin):
    # inlines = (QuestionInline,) #Para Agregar el formulario de las pregunatas al formulario de seccion
    # list_display = ('pk', 'user', 'section')
    # list_display_links = ('pk','user',)
    # list_editable = ('name',)
    # search_fields = ('name', 'pk', 'user__username')
    # # list_filter = ('created', 'modified')

    # # readonly_fields = ('created', 'modified')

# class AnswerInline(admin.StackedInline):
#     model = Answer
#     can_delete = False
#     verbose_name_plural = 'Answers'

# # @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     inlines = (AnswerInline,)
#     list_display = ('pk','question')
    # list_display_links = ('pk',)
    # list_editable = ('question',)
    # search_fields = ('question', 'pk', 'Section__name')

# @admin.register(Answer)
# class AnswerAdmin(admin.ModelAdmin):
#     list_display = ('pk','question','answer')
#     list_display_links = ('pk',)
#     list_editable = ('answer',)
#     search_fields = ('answer', 'pk', 'question__question')

# #Re-Register  UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# admin.site.register(Section,SectionAdmin)
# admin.site.register(Question,QuestionAdmin)


