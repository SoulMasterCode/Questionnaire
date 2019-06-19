# Rutas del Usuario

# Django
from django.urls import path

# views
from users import views

# Class Based Views 

urlpatterns = [
    path('login', views.login_view, name='loginUser'),
    path('logout', views.logout_view,name='logout'),
    path('singup', views.SignUpView.as_view(),name='signup'),
    path('update_profile', views.UpdateView.as_view(),name='update'),
]