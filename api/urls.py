from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls import include, url
from .views import UserViewSet, GroupViewSet, FeedbackViewSet, MeetingViewSet, UserGroupMappingViewSet, group_details_of_user, feedbacks_of_user, users_of_group, meetings_of_group


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)
<<<<<<< HEAD
router.register('feedback', views.FeedbackViewSet)
=======
router.register('usergroupmapping', UserGroupMappingViewSet)
router.register('feedback', FeedbackViewSet)
>>>>>>> master
router.register('meetings', MeetingViewSet)

urlpatterns = [
    path('', include(router.urls)),
<<<<<<< HEAD

=======
    path('users/<int:user_id>/group/', group_details_of_user),
    path('users/<int:user_id>/feedbacks/', feedbacks_of_user),
    path('groups/<int:group_id>/users/', users_of_group),
    path('groups/<int:group_id>/meetings/', meetings_of_group),
>>>>>>> master
]