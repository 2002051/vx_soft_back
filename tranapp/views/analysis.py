## 数据分析相关路由


# views.py

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse,redirect

def BookStatistics(request):
    """图书统计页"""
    print(request.COOKIES)
    sessionID = request.COOKIES.get("sessionid")
    if not sessionID:
        return redirect("/admin/")


    return render(request,"satistics/BookStatistics.html")
