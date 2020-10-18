from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserViewSet, GroupViewSet, FeedbackViewSet, MeetingViewSet, get_loggedin_user_details, \
    group_details_of_user, feedbacks_of_user, meetings_of_user, users_of_group, meetings_of_group \
    , set_meeting, set_user_availability, update_or_create_user, give_feedback

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)
router.register('feedbacks', FeedbackViewSet)
router.register('meetings', MeetingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('loggedinuser/', get_loggedin_user_details),
    path('update_or_create_user/', update_or_create_user),
    path('give_feedback/', give_feedback),
    path('users/<int:user_id>/group/', group_details_of_user),
    path('users/<int:user_id>/feedbacks/', feedbacks_of_user),
    path('users/<int:user_id>/meetings/', meetings_of_user),
    path('users/<int:user_id>/set_availability/', set_user_availability),
    path('groups/<int:group_id>/users/', users_of_group),
    path('groups/<int:group_id>/meetings/', meetings_of_group),
    path('groups/<int:group_id>/set_meeting/', set_meeting),
]