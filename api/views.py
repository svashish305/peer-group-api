from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from rest_framework import viewsets
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
            permission_classes = [AllowAny]
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
    # permission_classes = (IsAuthenticated,)


class UserGroupMappingViewSet(viewsets.ModelViewSet):
    queryset = UserGroupMapping.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AllowAny,)


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    # permission_classes = (IsAuthenticated,)


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = (IsAuthenticated,)
