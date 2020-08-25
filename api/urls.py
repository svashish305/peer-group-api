from django.urls import path
from rest_framework import routers
from django.conf.urls import include, url
from .views import UserViewSet, GroupViewSet, FeedbackViewSet, MeetingViewSet, get_loggedin_user_details, group_details_of_user, feedbacks_of_user, meetings_of_user, users_of_group, meetings_of_group\
    # , UserGroupMappingViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)
# router.register('usergroupmapping', UserGroupMappingViewSet)
router.register('feedbacks', FeedbackViewSet)
router.register('meetings', MeetingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('loggedinuser/', get_loggedin_user_details),
    path('users/<int:user_id>/group/', group_details_of_user),
    path('users/<int:user_id>/feedbacks/', feedbacks_of_user),
    path('users/<int:user_id>/meetings/', meetings_of_user),
    path('groups/<int:group_id>/users/', users_of_group),
    path('groups/<int:group_id>/meetings/', meetings_of_group),
]