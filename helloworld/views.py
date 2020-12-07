from django.shortcuts import render, HttpResponse


def helloworld(request):
    return HttpResponse(request, 'hello world')
