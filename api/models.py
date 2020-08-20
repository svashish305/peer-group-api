import jwt

from datetime import datetime, timedelta

from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, Group, PermissionsMixin
)
import random


# Create your models here.
class GroupExtend(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    groupName = models.CharField(max_length=200)

    def __str__(self):
        return self.groupName


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, role and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, role and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True

        user.save(using=self._db)

        # groups = GroupExtend.objects.all()
        # randomgroup = random.choice(groups)

        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # groupId = models.ForeignKey(GroupExtend, on_delete=models.CASCADE)
    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().

        The `@property` decorator above makes this possible. `token` is called
        a "dynamic property".
        """
        return self._generate_jwt_token()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')


class Feedback(models.Model):
    grade = models.CharField(max_length=200)
    remarks = models.CharField(max_length=200)
    receiverId = models.ForeignKey(MyUser, on_delete=models.CASCADE)


class Meeting(models.Model):
    groupId = models.ForeignKey(GroupExtend, on_delete=models.CASCADE)
    user = models.ManyToManyField(MyUser)
    url = models.CharField(max_length=200, default=False, blank=False)
    time = models.DateTimeField(auto_now=False)
