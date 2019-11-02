from rest_framework.permissions import BasePermission


class WordPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        """Здесь obj - экземпляр Word"""

        if request.user == obj.user:
            return True
