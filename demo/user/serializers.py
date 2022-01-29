from user.models import User,Music
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
     class Meta:
         model = User
         fields = '__all__'



class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'
        # fields = ('id', 'song', 'singer', 'last_modify_date', 'created')