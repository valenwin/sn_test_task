from rest_framework import serializers

from .models import User
from .utils import email_verify


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')

    def create(self, validated_data):
        password = validated_data.pop("password")
        check_email = email_verify(validated_data['email'])
        user = User.objects.create(**validated_data)
        if password and check_email:
            user.set_password(password)
            user.is_staff = True
            user.save()
        return user
