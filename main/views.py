from django.shortcuts import render, get_object_or_404, redirect
from main.models import Blog
from login.models import Account########login에 저장되어 있는 것을 main으로 가져옴
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def main(request):
    blog = Blog.objects
    text = ""
    if request.user.is_authenticated:
        txt_prime=Account.objects.get(user=request.user) #######
        text = txt_prime.nickname + "님 안녕하세요!" ##########ppt에 없음!
    else :
        text = "로그인해주세요!"
    return render(request, 'main.html', {'blog':blog, 'txt':text}) #, 'login':now_login

def other(request):
    return render(request, 'other.html')

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html',{'blog':blog_detail})

def news(request):
    return render(request, 'news.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def delete(request):
    del_id = request.GET['blogNum']
    blog = Blog.objects.get(id=del_id)
    blog.delete()
    return redirect("http://127.0.0.1:8000/")

def port(request):
    return render(request, 'portfolio.html')
# Create your views here.


@login_required
def blog_like(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id) 
        # post id에 해당하는 게시물
    user = request.user 
        # 현재 로그인한 user
    account = Account.objects.get(user=user) 
        # 현재 로그인한 user의 Account

    check_like_blogs = account.like_blogs.filter(id=blog_id)
        # 현재 로그인한 user가 좋아요한 게시글 중 현재 게시글이 있는지 체크

    if check_like_blogs.exists():
        if blog.like_num ==0:
            pass
        else:
            account.like_blogs.remove(blog)
            blog.like_num -= 1
            blog.save()
    
    else :
        account.like_blogs.add(blog)
        blog.like_num += 1
        blog.save()

    return render(request, 'detail.html')
    



