from django.urls import path
from rest_framework import routers
from django.conf.urls import include, url
from .views import UserViewSet, GroupViewSet, FeedbackViewSet, MeetingViewSet, RegistrationAPIView, LoginAPIView, \
    UserRetrieveUpdateAPIView

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)
router.register('feedback', FeedbackViewSet)
router.register('meetings', MeetingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user', UserRetrieveUpdateAPIView.as_view()),
    url('users/register', RegistrationAPIView.as_view()),
    url('users/login/', LoginAPIView.as_view()),
]