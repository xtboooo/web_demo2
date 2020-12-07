from django.shortcuts import render, HttpResponse


def register(request):
    """注册 View 视图函数"""
    return render(request, 'register.html')
