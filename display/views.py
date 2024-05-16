from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def calculate():
        y=1
        x=2
        return x

def say_helloworld(request):
    x = calculate()
    return render(request, 'hello.html')