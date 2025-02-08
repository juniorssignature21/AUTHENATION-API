from djoser import serializers 
from django.contrib.auth import get_User_model

User = get_User_model()

class UserCreateSerializer(serializers.UserCreateSerializer):
    class Meta(serializers.UserCreateSerializer.Meta):
     model = User   
     fields = {'id','email','password', 'username','first_name','last_name'}
