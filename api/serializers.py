from rest_framework import serializers
from .models import MyUser, GroupExtend, Feedback, Meeting
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = MyUser.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupExtend
        fields = {'id', 'groupName'}


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'grade', 'remarks', 'receiverId')


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ('id', 'url', 'time', 'groupId')
