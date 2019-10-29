# 데이터 처리 대상 : 모델, serializer import 시키기
from post.models import Post
from post.serializer import PostSerializer

from rest_framework import viewsets

# @action처리
from rest_framework import renderers
from rest_framework.decorators import action
from django.http import HttpResponse  #내가 임의로 만드는 view니깐 

'''
# ReadOnlyModelViewSet은 말 그대로 ListView, DetailView의 조회만 가능
class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
'''

#ModelViewSet은 ListView와 DetailView에 대한 CRUD가 모두 가능

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    #@action(method=['post'])
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) # @ + 함수들 > decorator, 장식자
    # 얍 띄우는 custom api
    def highlight(self, request, *args, **kwargs):
        return HttpResponse("얍") # 직접 response 만들어 보겠다

"""
action decorator(장식자)
Viewset을 통해 CRUD를 간단하게 구현하고 내가 원하는 기능(다른 logic)은 어떻게 구현하지?
나만의 Custom API를 구현하는 방법
@action()
def fnc()

rendering : Response를 어떤 형식으로 Rendering 시킬 것인가
ex) renderer.JSONRenderer >> JSON방식으로 렌더링 (default renderer1)
ex) renderer.BrowsableAPIRenderer >> 지금까지 봐온 브라우저상의 렌더링 (default renderer2)
etc) 있지만 굳이 기억할 필요x

어떤 Method로 처리가 될까?
>> Custom API의 Default Method는 GET방식이다
>> Action의 format인자로 지정 가능하다!
"""
