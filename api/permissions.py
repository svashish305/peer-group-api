from rest_framework import permissions
from .models import MyGroup


def _is_in_group(user, group_id):
    """
    Takes a user and a group id, and returns `True` if the user is in that group.
    """
    try:
        return MyGroup.objects.get(id=group_id).user_set.filter(id=user.id).exists()
    except MyGroup.DoesNotExist:
        return None


def _has_group_permission(user, required_groups):
    return any([_is_in_group(user, group_name) for group_name in required_groups])


class IsLoggedInUserOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # required_groups = [MyGroup.objects.get(id=request.user.group_id)]
        # has_group_permission = _has_group_permission(request.user, self.required_groups)
        # if self.required_groups is None:
        #     return False
        return obj == request.user or request.user.is_staff \
            # or has_group_permission


class IsAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        # has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and request.user.is_staff and (not request.user.is_student) \
            # and has_group_permission

    def has_object_permission(self, request, view, obj):
        # has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and request.user.is_staff \
            # and has_group_permission


class IsAdminOrAnonymousUser(permissions.BasePermission):
    required_groups = ['admin', 'anonymous']

    def has_permission(self, request, view):
        # has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user \
            # and has_group_permission


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user


class IsTeacherAndLoggedIn(permissions.BasePermission):
    def has_permission(self, request, view):
        # has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and (not request.user.is_student) \
            # and has_group_permission

    # def has_object_permission(self, request, view, obj):
    #     # has_group_permission = _has_group_permission(request.user, self.required_groups)
    #     return obj == request.user and request.user and (not request.user.is_student) \
    #         # and has_group_permission
