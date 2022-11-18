from rest_framework import permissions
from .premissions import IsStaffEditorPermission

class StaffEditorPermissionMixin():
    premission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    