from django.shortcuts import render
from .models import blog

def allblogs(request):
    blogs = blog.objects
    return render(request,"blog/allblogs.html",{'blogs':blogs})