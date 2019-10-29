#classcrud.views

from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic.list import ListView  # 데이터 보여주기
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # 데이터 추가
from .models import ClassBlog

class BlogView(ListView):  #html 템플릿이 필요함 >> 함수로 정의할 때는 return render (수행결과)
    # template_name = 'classcrud_list.html' >> 내가 원하는 이름으로 바꾸는 코드 url 바꾸기위함
    model = ClassBlog # 블로그 리스트를 담는 html 필요 : (소문자모델)_list.html

class BlogCreate(CreateView): # 입력 form을 갖고 있는 html 필요 : (소문자모델)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')#redirect 기능 ()안에는 url path 이름을 넣으면 된다.

class BlogDetail(DetailView):
    model = ClassBlog

class BlogUpdate(UpdateView):
    model = ClassBlog
    fields= ['title', 'body']
    success_url = reverse_lazy('list')

class BlogDelete(DeleteView): #진짜로 지울지 경고 및 확인 메세지를 담은 html 필요 : (소문자모델)_confirm_delete.html
    model = ClassBlog
    success_url = reverse_lazy('list')