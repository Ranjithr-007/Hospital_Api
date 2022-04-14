from rest_framework import serializers
from .models import *

class UserRegister(serializers.ModelSerializer):
    
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    
    class Meta:
        model=CustomUser
        fields=["username","password","phone","password2"]
        
    def save(self):
        reg=CustomUser(
            phone=self.validated_data['phone'],
            username=self.validated_data['username'],
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'password':'password does not match'})
        reg.set_password(password)
        reg.save()
        return reg
    
class UserDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=CustomUser
        fields=['username','phone','first_name','last_name']