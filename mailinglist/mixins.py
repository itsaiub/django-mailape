from django.core.exceptions import PermissionDenied, FieldDoesNotExist
from . import models


class UserCanUseMailingList:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        user = self.request.user
        if isinstance(obj, models.MailingList):
            if obj.user_can_use_mailing_list(user):
                return obj
            else:
                raise PermissionDenied()

        mailig_list_attr = getattr(obj, 'mailing_list')
        if isinstance(mailig_list_attr, models.MailingList):
            if mailig_list_attr.user_can_use_mailing_list(user):
                return obj
            else:
                raise PermissionDenied()
        raise FieldDoesNotExist('view does not know how to get mailing list')
