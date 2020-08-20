from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from .admin import StudentSignUpForm, TeacherSignUpForm
from .models import MyUser, GroupExtend, Feedback, Meeting
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser
from .serializers import UserSerializer, GroupSerializer, FeedbackSerializer, MeetingSerializer


# Create your views here.
class TeacherSignUpView(CreateView):
    model = MyUser
    form_class = TeacherSignUpForm

    def get_context_data(self, **kwargs):
        kwargs['role'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('teachers:quiz_change_list')


class StudentSignUpView(CreateView):
    model = MyUser
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['role'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('students:quiz_list')


class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = GroupExtend.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = (IsAuthenticated,)


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    # permission_classes = (IsAuthenticated,)


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = (IsAuthenticated,)
