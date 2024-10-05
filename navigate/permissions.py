from rest_framework import permissions

class IsMosqueAdmin(permissions.BasePermission):
    """
    Custom permission to only allow mosque admins to view or edit their mosque and prayers.
    """
    
    def has_object_permission(self, request, view, obj):
        # Check if the user is the mosque admin for the object
        return obj.mosqueAdmin == request.user