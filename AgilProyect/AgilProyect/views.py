from django.http import HttpResponse
from django.http import JsonResponse

def hello_world(request):
    return HttpResponse('<h1>Hello django</h1>')

def numbers(request):
    numb = request.GET['numbers']
    numeros = sorted(numb.split(','))
    return JsonResponse(numeros, safe=False)
   