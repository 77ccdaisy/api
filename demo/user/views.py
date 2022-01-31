from crypt import methods
from django import views
from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from user.serializers import MusicSerializer,ShareSerializer
from user.models import Music,Share

from rest_framework import viewsets
from rest_framework import generics


# viewsets.ModelViewSet 含有ＣＲＵＤ Ｌ功能
# A viewset that provides default create(), retrieve(), update(), partial_update(), destroy() and list() actions.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = (IsAuthenticated,) #設定權限才可使用



class ShareViewSet(viewsets.ModelViewSet):
    queryset = Share.objects.all()
    serializer_class = ShareSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

# IsAuthenticated : 需要用戶登錄才能存取
# IsAdminUser: 需要為django superuser才能存取
# IsAuthenticatedOrReadOnly: 不用登錄即可取得資料，但修改資料需要登錄
# 默認 AllowAny允許不受限制的訪問，無論請求是經過身份驗證還是未經身份驗證。

