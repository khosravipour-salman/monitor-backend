from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from helpers import helpers
from accounting import managers


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=15, unique=True, null=False)
    role = models.CharField(choices=helpers.USER_ROLE_CHOICES, max_length=7, null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = managers.UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.phone_number} - {self.get_role_display()}'

    @property
    def is_staff(self):
        return self.is_superuser


# class InternProxy(User):
#     base_role = helpers.INTERN
#     objects = managers.InternManager()

#     class Meta:
#         proxy = True

#     # model methods here!
#     # get work_logs and so on ...

# class InternProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     emergency_phone = models.CharField(max_length=15, null=True, blank=True)
#     home_number = models.CharField(max_length=15, null=True, blank=True)  # make it unique later
#     fullname = models.CharField(max_length=80)
#     address = models.TextField(null=True, blank=True)
#     gender = models.BooleanField(null=True, blank=True)
#     birth_date = models.DateTimeField(null=True, blank=True)
#     city = models.CharField(max_length=40)  # محل صدور شناسنامه
#     military_service = models.CharField(choices=helpers.MILITARY_STATUS_CHOICES, max_length=80)  # وضعیت خدمت
#     national_code = models.PositiveIntegerField(null=True, blank=True)  # add validation year / make it unique later
#     email = models.EmailField(null=True, blank=True)
#     marital = models.BooleanField(default=False, null=True, blank=True)

#     def __str__(self):
#         return self.fullname


# class EducationInfo(models.Model):
#     pass



