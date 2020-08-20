from django.contrib.auth import login
from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import MyUser, MyGroup, Feedback, Meeting, UserGroupMapping
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser
from .serializers import UserSerializer, GroupSerializer, FeedbackSerializer, MeetingSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            # permission_classes = [AllowAny]
            permission_classes = [IsAdminUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [AllowAny]
            # permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            # permission_classes = [IsAdminUser]
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = MyGroup.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated,)


class UserGroupMappingViewSet(viewsets.ModelViewSet):
    queryset = UserGroupMapping.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AllowAny,)


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
<<<<<<< HEAD
    permission_classes = (AllowAny,)

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
=======
    permission_classes = (IsAuthenticated,)
>>>>>>> master


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
<<<<<<< HEAD
    permission_classes = (AllowAny,)

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
=======
    permission_classes = (IsAuthenticated,)


@api_view(['GET'])
def group_details_of_user(request, user_id):
    user = MyUser.objects.get(id=user_id)
    groupId = user.groupId.id
    group = MyGroup.objects.get(id=groupId)
    return render(request, 'group_details.html', {'group': group})

@api_view(['GET'])
def feedbacks_of_user(request, user_id):
    user = MyUser.objects.get(id=user_id)
    feedbacks = Feedback.objects.filter(receiverId=user)
    return render(request, 'feedbacks.html', {'feedbacks': feedbacks})

@api_view(['GET'])
def users_of_group(request, group_id):
    group = MyGroup.objects.get(id=group_id)
    users = MyUser.objects.filter(groupId=group)
    return render(request, 'users_of_group.html', {'users': users})

@api_view(['GET'])
def meetings_of_group(request, group_id):
    group = MyGroup.objects.get(id=group_id)
    meetings = Meeting.objects.filter(groupId=group)
    return render(request, 'meetings_of_group.html', {'meetings': meetings})
>>>>>>> master
