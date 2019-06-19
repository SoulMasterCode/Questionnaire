#django
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError 
from django.urls import reverse_lazy, reverse

# Class Vased Views
from django.views.generic import DetailView
from django.views.generic import FormView, UpdateView

#authentificate
from django.contrib.auth import authenticate, login, logout

#models
from django.contrib.auth.models import User
from users.models import Profile

#Forms
from users.forms import *

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        passwd = request.POST['password']
        user = authenticate(request, username=user_name, password=passwd)

        if user is not None:
            login(request, user)
            return redirect('questionary:questionnaires')
        else:
            return render(request,'users/login.html',{'error':'incorrect password or user'})
    
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('users:loginUser')

# def signup_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirmpass= request.POST['confirmpass']
#         phonenumber = request.POST['phonenumber']

#         if password == confirmpass:
#             try:
#                 user = User.objects.create_user(username, email, password)
#             except IntegrityError:
#                 return render(request, 'users/signup.html',{'error':'Usuario Existente'})
#             profile = Profile(user=user, phone_number=phonenumber)
#             profile.save()
#             return redirect('users:loginUser')
#         else:
#             return render(request, 'users/signup.html',{'error':'Contraseña Incorrecta'})
#     return render(request,'users/signup.html')

class SignUpView(FormView):
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:loginUser')
    form_class = SignupForm
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    


# def update_view(request):
#     profile = request.user.profile
#     user = request.user

#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)

#         if form.is_valid():
#             data = form.cleaned_data

#             user.first_name = data['first_name']
#             user.last_name = data['last_name']
#             profile.phone_number = data['phone_number']
            
#             if not data['picture'] is None:
#                 profile.picture = data['picture']

#             user.save()
#             profile.save()

#             return redirect('users:update')
        
#     else:
#         form = ProfileForm()
            
#     return render(request, 'users/update.html',{'profile':profile, 'user':user, 'form':form})

class UpdateView(UpdateView):
    template_name = 'users/update.html'
    form_class = ProfileForm
    model = Profile
    
    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile."""
        return reverse('questionary:questionnaires')


# class LoginView(ListView):
#     model = User
#     template_name = 'users/login.html'

#     def get(self, request):
#         return render(request, self.template_name)

#     def post(self, request):
#         user_name = request.POST['username']
#         passwd = request.POST['password']
#         user = authenticate(request, username=user_name, password=passwd)

#         if user is not None:
#             login(request, user)
#             return redirect(request, 'dictionary')
#         else:
#             return render(request,self.template_name,{'error':'incorrect password or user'})
