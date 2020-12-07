from django.shortcuts import render, HttpResponse
from users.models import User
from users.common import get_md5_pwd

def register(request):
    """注册 View 视图函数"""
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f'username:{username} password:{password}')
        password = get_md5_pwd(password)
        user = User.objects.create(username=username, password=password)
        return HttpResponse('注册成功')
