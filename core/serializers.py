from rest_framework import serializers
from .models import Post
from account.serializers import RegisterSerializer
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','content']
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["created_at"] = instance.created_at
        data["user"] = RegisterSerializer(instance.user).data
        return data