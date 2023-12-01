from rest_framework import permissions
from profiles import views


class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    return obj.owner == request.user


# class HasPostedOrReadOnly(permissions.BasePermission):
#   def has_object_permission(self, request, view, obj):
#     if request.method in permissions.SAFE_METHODS:
#       return True
#     if profile.owner.posts_count != 0:
#         return obj.owner == request.user



    