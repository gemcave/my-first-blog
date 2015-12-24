# from rest_framework.permissions import BasePermission, SAFE_METHODS
# from django.contrib.auth.models import User


# class IsOwner(BasePermission):
# 	def has_object_permission(self, request, view, obj):
# 		'''Проверка прав'''

# 		if request.method in SAFE_METHODS:
# 			return True
# 		elif request.method == 'PUT' or request.method == 'PATCH' or request.method == 'DELETE':
# 			if obj.author == request.user:
# 				return True
# 			return False
from rest_framework import permissions

class IsAuthenticatedOrCreate(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return super(IsAuthenticatedOrCreate, self).has_permission(request, view)