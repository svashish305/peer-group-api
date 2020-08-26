from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import MyUser, MyGroup, Feedback, Meeting
from .permissions import IsAdminUser, IsTeacherAndLoggedIn
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
    permission_classes = (IsAuthenticated, IsTeacherAndLoggedIn)


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (IsAuthenticated, IsTeacherAndLoggedIn)


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = (IsAuthenticated, IsTeacherAndLoggedIn)


@api_view(['GET'])
def get_loggedin_user_details(request):
    user = {
        'id': request.user.id,
        'email': request.user.email,
        'is_student': request.user.is_student,
        'groupId': request.user.groupId.id
    }
    return JsonResponse(user, safe=False)


@api_view(['GET'])
def group_details_of_user(request, user_id):
    user = MyUser.objects.get(id=user_id)
    group_id = user.groupId.id
    group = MyGroup.objects.get(id=group_id)
    group_details = {
        'id': group.id,
        'groupName': group.groupName
    }
    return JsonResponse(group_details, safe=False)


@api_view(['GET'])
def feedbacks_of_user(request, user_id):
    if request.user.id == user_id:
        user = MyUser.objects.get(id=user_id)
        feedbacks = list(Feedback.objects.filter(receiverId=user).values())
        return JsonResponse(feedbacks, safe=False)
    else:
        if request.user.is_student:
            return HttpResponse("You can't access this info")
        else:
            user = MyUser.objects.get(id=user_id)
            feedbacks = list(Feedback.objects.filter(receiverId=user).values())
            return JsonResponse(feedbacks, safe=False)


@api_view(['GET'])
def users_of_group(request, group_id):
    group = MyGroup.objects.get(id=group_id)
    users = list(MyUser.objects.filter(groupId=group).values("id", "email", "is_student"))
    return JsonResponse(users, safe=False)


@api_view(['GET'])
def meetings_of_group(request, group_id):
    group = MyGroup.objects.get(id=group_id)
    meetings = list(Meeting.objects.filter(groupId=group).values())
    return JsonResponse(meetings, safe=False)


@api_view(['GET'])
def meetings_of_user(request, user_id):
    user = MyUser.objects.get(id=user_id)
    meetings = list(Meeting.objects.filter(groupId=user.groupId.id).values())
    return JsonResponse(meetings, safe=False)
