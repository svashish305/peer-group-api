from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, Group, GroupManager, PermissionsMixin
)
import random

# Create your models here.
class MyUserManager(BaseUserManager, PermissionsMixin):
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

        # randomGroup = random.choice(Group.objects.all())
        # user.groupId = Group.objects.get(name=randomGroup.name).id

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
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    # groupId = models.ForeignKey(Group, on_delete=models.CASCADE)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

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



# class Feedback(models.Model):

class Meeting(models.Model):
    # groupId = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ManyToManyField(MyUser)
    meetingUrl = models.CharField(max_length=200,default=False,blank=False)
    meetingTime = models.DateTimeField(auto_now=False)

    
