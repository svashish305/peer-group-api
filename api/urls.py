from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls import include
from .views import UserViewSet, GroupViewSet, FeedbackViewSet, MeetingViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)
router.register('feedback', views.FeedbackViewSet)
router.register('meetings', MeetingViewSet)

urlpatterns = [
    path('', include(router.urls)),

]