from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.db import transaction
from rest_framework.generics import GenericAPIView
from user.serializers import UserSerializer ,MusicSerializer
from user.models import User,Music

from rest_framework import viewsets


# 繼承 Django REST framework 的 GenericAPIView 實現 UsersView 的 get（獲得 user 列表） 以及 post （創建 user）的方法。
class UsersView(viewsets.ModelViewSet):
    queryset = User.objects.all() #取得User table全部資料
    serializer_class = UserSerializer #等下要去拿去轉換模型的類型的方法
    # def get(self, request, *args, **krgs): #設定get取得方法
    #     users = self.get_queryset()
    #     serializer = self.serializer_class(users, many=True)#設定取得的models.py 類型,取得Uset經過序列化器 轉換可傳輸的模式資料
    #     data = serializer.data
    #     return JsonResponse(data, safe=False) # return json格式
    # def post(self, request, *args, **krgs):
    #     data = request.data
    #     try:
    #         serializer = self.serializer_class(data=data)
    #         serializer.is_valid(raise_exception=True)
    #         with transaction.atomic():
    #             serializer.save()
    #         data = serializer.data
    #     except Exception as e:
    #         data = {'error': str(e)}
    #     return JsonResponse(data)


# viewsets.ModelViewSet 含有ＣＲＵＤ Ｌ功能
# A viewset that provides default create(), retrieve(), update(), partial_update(), destroy() and list() actions.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer