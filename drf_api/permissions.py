from rest_framework import permissions
from profiles import views
from posts.serializers import PostSerializer


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

class CustomPermission(permissions.BasePermission):
  message = 'You must post your own work in order to leave reviews'

  def has__object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
      user = User.objects.get(id=self.request.user.id)
      user_posts = Post.objects.get(owner=user).count()
    if user_posts != 0:
      return True
    return False 
    


   
   
    



    