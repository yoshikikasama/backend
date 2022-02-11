from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate,login,logout
from .models import ReviewModel
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.

def signupview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        passwordname_data = request.POST['passwordname_data']
        try:
            User.objects.create_user(username_data,'',passwordname_data)
        except IntegrityError:
            return render(request,'signup.html',{'error':'このユーザーは既に登録されています'})
    else:
        #ユーザーテーブルのデータの全て表示
        #print(User.objects.all())   
        return render(request,'signup.html',{})

    return render(request,'signup.html',{})
def loginview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        passwordname_data = request.POST['passwordname_data']
        user = authenticate(request,username = username_data,password = passwordname_data )
        if user is not None:
            login(request,user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request,'login.html')
@login_required
def listview(request):
    #ReviewModelの中の全てのデータの格納
    object_list = ReviewModel.objects.all()
    return render(request,'list.html',{'object_list' : object_list})
#pkを引数に指定することでURLで指定した番号を受け取る
@login_required
def detailview(request,pk):
    #ReviewModelの中のpkに合致するデータを持ってくる
    detail_object = ReviewModel.objects.get(pk=pk)
    return render(request,'detail.html',{'object' : detail_object})

class CreateClass(CreateView):
    template_name = 'create.html'
    model = ReviewModel
    fields = {'title','content','author','images','evaluation'}
    success_url = reverse_lazy('list')
def logoutview(request):
    logout(request)
    return redirect('login')
    
def evaluationview(request,pk):
    post = ReviewModel.objects.get(pk=pk)
    author_name =request.user.get_username() + str(request.user.id)
    if author_name in post.useful_review_record:
        return redirect('list')
    else:
        post.useful_review = post.useful_review+1
        post.useful_review_record =  post.useful_review_record + author_name
        post.save()
        return redirect('list')