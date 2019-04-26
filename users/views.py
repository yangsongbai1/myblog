from django.shortcuts import render
from .models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse


def login_view(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            messages.error(request, '用户名或密码不能为空！')
            return render(request, 'users/login.html')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user and user.is_active:
            # login(request, user)
            messages.success(request, '登录成功')
            print('登录成功')
            return render(request, 'article/index.html')
        else:
            messages.error(request, '用户名或密码错误')
            print('用户名或密码错误')
            return render(request, 'users/login.html')

def register_view(request):
    username = '12345'
    password = '54321'
    telephone = '12345678912'
    user = User.objects.create_user(telephone=telephone, username=username, password=password)
    print(user.username)
    return HttpResponse('successful')