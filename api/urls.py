from django.urls import path
from rest_framework import routers
from django.conf.urls import include, url
from .views import UserViewSet, GroupViewSet, FeedbackViewSet, MeetingViewSet, UserGroupMappingViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)
router.register('usergroupmapping', UserGroupMappingViewSet)
router.register('feedback', FeedbackViewSet)
router.register('meetings', MeetingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]