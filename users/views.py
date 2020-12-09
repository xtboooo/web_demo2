from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from users.models import User
from users.common import get_md5_pwd


def register(request):
    """注册 View 视图函数"""
    if request.method == 'GET':
        return render(request, 'register.html', )
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f'username:{username} password:{password}')

        # 先导入get_md5_pwd, 传入password, 获取md5加密后的密码
        # password = get_md5_pwd(password)

        user = User.objects.create(username=username, password=password)
        return redirect('/login/')


def login(request):
    if request.method == 'GET':
        cooki_username = request.COOKIES.get('username', '')
        username = cooki_username.encode('ISO-8859-1').decode('utf-8')
        return render(request, 'login.html', locals())
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return JsonResponse({'message': 'login failed'})
        else:
            response = JsonResponse({'message': 'login success'})
            if remember == 'true':
                username = bytes(username, 'utf-8').decode('ISO-8859-1')
                response.set_cookie('username', username, max_age=14 * 24 * 3600)
            return response