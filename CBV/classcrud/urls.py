#classcrud.urls

from django.urls import path
from classcrud import views

urlpatterns = [
    path('',views.BlogView.as_view(),name='list'),
    path('newblog/',views.BlogCreate.as_view(),name='new'),
    path('detail/<int:pk>',views.BlogDetail.as_view(),name='detail'),
    path('update/<int:pk>',views.BlogUpdate.as_view(),name='change'),
    path('delete/<int:pk>',views.BlogDelete.as_view(),name='del'),
]
# .as_view() : 앞서서 정의되는 class method : 상속받은 ListView , CreateView, UpdateView, DeleteView에서 default로 저장되어있는 메소드
# 정확히는 django.views.generic 의 base.py에 존재 ~view들은 이를 통해 만들어진것
# .as_view()의 필요성: path 라는 함수는 3가지 인자 받음(url의 이름, 함수 , urlpath의 이름)
