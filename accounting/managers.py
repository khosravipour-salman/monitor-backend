from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

from accounting import models
from helpers import helpers

class UserManager(BaseUserManager):
    def _create_user(self, phone_number, password, **kwargs):
        user = self.model(
            phone_number=phone_number,
            last_login=timezone.now(),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_intern(self, phone_number, password, **kwargs):
        user = self._create_user(phone_number, password, **kwargs)
        user.role = helpers.INTERN
        user.save(using=self._db)
        return user


    def create_superuser(self, phone_number, password, **kwargs):
        user = self._create_user(phone_number, password, **kwargs)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class InternManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=helpers.INTERN)

    def create(self, user, **kwargs):
        if not user.role == helpers.INTERN:
            raise ValidationError('"User" object must have "intern" role.')

        user = models.InternProfile.objects.create(user=user, **kwargs)
        user.save()
        return user