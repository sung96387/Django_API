from rest_framework.routers import DefaultRouter
from django.urls import include, path
from post import views

#라우터가 없다면?

router=DefaultRouter()
router.register('post',views.PostViewSet)

urlpatterns=[
    path('',include(router.urls))
]

#하나의 path로 CRUD를 모두 처리할 수 있을까? NO >> pk 가 필요한 경우도 있기 때문