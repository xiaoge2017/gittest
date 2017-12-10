from django.shortcuts import render
from app01 import models
# Create your views here.
def git1(request):
    gituser=models.gituser.objects.filter().all()
    return render(request,'git1.html',{'gituser':gituser})