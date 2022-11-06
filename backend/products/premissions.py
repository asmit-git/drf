from rest_framework import permissions

'''
custom permissions comes in handy when we have to secure the get method as well.
Generally DjangoModelPremission secures the action routes that is create,update and delete.
For List route we will have to create custom permission by overriding default in DjangoModelPremissions
'''

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    '''
    overriding the DjangoModelPermission for GET Method
    '''
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],  #overridden code
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
    '''
    This very function below can be used in view for permission as
    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]
    '''
    # def has_permission(self, request, view):
    #     if not request.user.is_staff:
    #         return False
    #     return super().has_permission(request, view)

    # def has_permission(self, request, view):
    #     user = request.user
    #     print(user.get_all_permissions())
    #     # return super().has_permission(request, view)
    #     if request.user.is_staff:
    #         if user.has_perm("products.view_product"):  #"app_name.verb(action).model_name"
    #             return True
    #         if user.has_perm("products.add_product"):
    #             return True
    #         if user.has_perm("products.change_product"):
    #             return True
    #         if user.has_perm("products.delete_product"):
    #             return True
    #         return False
    #     return False

    # def has_object_permission(self, request, view, obj):
    #     # return super().has_object_permission(request, view, obj)
    #     pass