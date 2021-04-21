from rest_framework import serializers
from .models import User,Recital,Juki,Comment,Like,kamil

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'


class RecitalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recital
        fields='__all__'
        extra_fields='Recital'
    

class JukiSerializer(serializers.ModelSerializer):
    class Meta:
        model=Juki
        fields='__all__'
    

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'
   

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Like
        fields='__all__'


class KamilSerializer(serializers.ModelSerializer):
    class Meta:
        model=kamil
        fields='__all__'
        read_only_fields = ['jukiNumber','jukiType']

   
   