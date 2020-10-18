from rest_framework import serializers
from .models import MyUser, MyGroup, Feedback, Meeting


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        # fields = ('id', 'name', 'email', 'password', 'is_student', 'rating', 'group_id', 'availability')
        fields = ('id', 'name', 'email', 'password', 'is_student', 'group_id', 'availability', 'created_at', 'updated_at')
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = MyUser.objects.create_user(**validated_data)
        user.username = validated_data.get('email')
        user.name = validated_data.get('name')
        user.is_student = validated_data.get('is_student')
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        """Performs an update on a User."""

        # Passwords should not be handled with `setattr`, unlike other fields.
        # Django provides a function that handles hashing and
        # salting passwords. That means
        # we need to remove the password field from the
        # `validated_data` dictionary before iterating over it.
        password = validated_data.pop('password', None)

        for (key, value) in validated_data.items():
            # For the keys remaining in `validated_data`, we will set them on
            # the current `User` instance one at a time.
            setattr(instance, key, value)

        if password is not None:
            # `.set_password()`  handles all
            # of the security stuff that we shouldn't be concerned with.
            instance.set_password(password)

        # After everything has been updated we must explicitly save
        # the model. It's worth pointing out that `.set_password()` does not
        # save the model.
        instance.save()

        return instance


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyGroup
        fields = ('id', 'name', 'created_at', 'updated_at')


# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = ('id', 'problem_statement', 'problem_link')


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        # fields = ('id', 'grade', 'remarks', 'receiver_id')
        fields = ('id', 'remarks', 'receiver_id', 'created_at', 'updated_at')


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ('id', 'url', 'time', 'users', 'group_id', 'created_at', 'updated_at')
