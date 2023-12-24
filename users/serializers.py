from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import serializers

User=get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, max_length=20)
    team = serializers.CharField(required=True, max_length=20)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'team', 'password1', 'password2']
        extra_kwargs = {
            'password1': {'write_only': True},
            'password2': {'write_only': True}
        }

    def validate(self, data):
        password1 = data.get('password1')
        password2 = data.get('password2')

        if password1 != password2:
            raise serializers.ValidationError({"Error": "비밀번호가 일치하지 않습니다."})
        
        if User.objects.filter(username=data.get('username')).exists():
            raise serializers.ValidationError({"Error": "아이디가 이미 존재합니다."})
        
        return data

    def create(self, validated_data):
        username = validated_data.get('username')
        team = validated_data.get('team')
        password = validated_data.pop('password1')

        user = User.objects.create_user(username=username)
        user.team = team
        user.set_password(password)
        user.save()

        return user