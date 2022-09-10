from django.shortcuts import redirect, render
from django.contrib import auth # 로그인 기능과 로그아웃 기능 수행
from django.contrib.auth.models import User

def login(request):
    # post 요청이 들어오면 login 처리를 해주고
    if(request.method =='POST'):
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')

    # get 요청이 들어오면 login form을 담고 있는 login.html을 띄워주는 역할
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
