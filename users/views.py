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
    username = request.session.get('username')
    if username:
        return HttpResponse(f'{username} 用户已存在')
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return JsonResponse({'message': 'login failed'})
        else:
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            if remember == 'true':
                request.session.set_expiry(0)
            return JsonResponse({'message': 'login success'})
