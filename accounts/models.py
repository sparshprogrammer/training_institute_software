from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from simple_email_confirmation.models import SimpleEmailConfirmationUserMixin


class User(SimpleEmailConfirmationUserMixin, AbstractUser):
    objects = UserManager()

    class Meta(object):
        unique_together = ('email',)

#
# class UserProfile(models.Model):
#     user = models.OneToOneField(UserOver, on_delete=models.CASCADE)