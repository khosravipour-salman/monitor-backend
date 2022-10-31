from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
	message = 'Permission denied; admin only.'
	def has_permission(self, request, view):
		if request.method in SAFE_METHODS:
			return True

		return request.user.is_admin
