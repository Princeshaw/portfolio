from django.shortcuts import render,get_object_or_404
from .models import blog

def allblogs(request):
    blogs = blog.objects
    return render(request,"blog/allblogs.html",{'blogs':blogs})
def readblog(request,blog_id):
    detail = get_object_or_404(blog,pk=blog_id)
    return render(request,'blog/readblog.html',{'detail':detail})    