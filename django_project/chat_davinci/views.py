from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('Hello World!')

def chat(request):
    return render(request, 'index.html')