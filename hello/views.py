from django.http.response import HttpResponse
from django.shortcuts import render
from random import randint
# Create your views here.


def index(request):
    return HttpResponse("Hello")


def greeting(request, name):
    return render(request, 'hello/greet.html', {
        "name": name.capitalize(),
        "age": getRandomAge()
    })


def home(request):
    return render(request, 'hello/index.html')


def getRandomAge():
    ages = [1992, 1967, 2006, 1978, 1996, 1994, 1987, 1989, 2002, 2010]
    random_number = randint(0, len(ages) - 1)
    age = 2021 - ages[random_number]
    return age
