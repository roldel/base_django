from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello ! <br> <br> Here is some http content")


def tempview(request):
    return render(request, 'core/intro.html')