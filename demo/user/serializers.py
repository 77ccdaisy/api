from user.models import Music,Share
from rest_framework import serializers #序列器基類模塊
   

class MusicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'
        # fields = ('id', 'song', 'singer', 'last_modify_date', 'created')


class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Share
        fields = '__all__'


''' ModelSerializer 回傳id值  (get不會出現 url可點入編輯)
[
  {
    "id": 1,
    "email": "user@example.com",
    "name": "string"
  },
  {
    "id": 2,
    "email": "no2user@example.com",
    "name": "222string"
  }
]

HyperlinkedModelSerializer 回傳 url/{id}，url字段代替主要關键字字段

[
  {
    "url": "http://127.0.0.1:8000/api/user/1/",
    "email": "user@example.com",
    "name": "string"
  },
  {
    "url": "http://127.0.0.1:8000/api/user/2/",
    "email": "no2user@example.com",
    "name": "222string"
  }
]
'''


