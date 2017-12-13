from django.shortcuts import render,HttpResponse,redirect
from home import models
# Create your views here.

def login(request):
    if request.method=='POST':
        user=request.POST.get('user')
        pwd=request.POST.get('pwd')
        if models.Users.objects.filter(username=user,password=pwd):
            import datetime
            res=redirect('/home/index/')
            current_date=datetime.datetime.utcnow()
            res.set_cookie('home_user',user,expires=current_date,max_age=10)
            return res
        else:
            print('用户名或密码不正确请重新输入')
            return render(request,'login.html')
    elif request.method=='GET':
        return render(request,'login.html')
    else:
        return redirect('/home/login/')

def index(request):
    # v=request.COOKIES.get('home_user')
    # if v:
    #     obj=models.Users.objects.filter().all()
    #     return render(request, 'index.html', {'current_user': v,'obj':obj})
    obj = models.Users.objects.filter().all()
    return render(request, 'index.html', {'obj':obj})#测试使用
    # return redirect('/home/login/')
