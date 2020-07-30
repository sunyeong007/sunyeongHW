from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Account

# Create your views here.
def signup(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        pw1 = request.POST.get("password1")
        pw2 = request.POST.get("password2")
        email = request.POST.get("email")
        nickname = request.POST.get("nickname")

        #모든 정보를 입력했는지, 비밀번호와 비밀번호 확인이 맞게 이루어졌는지
        if user_id=="" or pw1=="" or pw2=="" or email=="" or nickname=="":
            messages.info(request, "빈칸을 채워주시오!")
            return redirect('signup')
        if pw1 != pw2 :
            messages.info(request, "비밀번호가 달라요!")
            return redirect('signup')
        #지금까지 과정은 유저가 정보를 제대로 입력했으면 그걸 다 가져오는 과정
        #정보를 받았으니까 그거에 db를 저장
        user = User.objects.create_user(username=user_id, password=pw1)#username, password는 장고에서 재공해주는 db에 있는 column내용
        user.save()

        account = Account(user=user, email=email, nickname=nickname) #user는 외래키(참조키)
        account.save()
        return redirect('main')###   
    else:
        return render(request, 'signup.html')
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        user_id = request.POST['user_id'] #있는지 없는지만 체크하면 되서 GET필요 없음
        password = request.POST['password']
        #login html에서 입력한정보랑 User DB랑 비교하는 과정
        user = auth.authenticate(request, username = user_id, password = password)#####################

        if user is not None:
            auth.login(request, user)
            return redirect('main')

        else:
            messages.info(request, '회원정보가 없어요!')
            return redirect('login')
            
    else:
        return render(request, 'login.html')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('main')