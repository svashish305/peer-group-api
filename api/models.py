from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


# Create your models here.


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MyGroup(Timestamp):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


def get_default_group():
    return MyGroup.objects.get(id=1)
    # return MyGroup.objects.get_or_create(name='White')


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, name=None, is_student=False, group_id=get_default_group()):
    # def create_user(self, email, password=None, name=None, is_student=False, group_id=1):
        """
        Creates and saves a User with the given email, role and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            is_student=is_student,
            group_id=group_id,
        )

        user.set_password(password)

        if user.is_student:
            user.save(using=self._db)
        elif not user.is_student:
            user.is_superuser = True
            user.is_admin = True

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
        user.is_student = False
        user.save(using=self._db)

        return user


class MyUser(AbstractBaseUser, PermissionsMixin, Timestamp):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    is_student = models.BooleanField(default=False, null=True)
    group_id = models.ForeignKey(MyGroup, on_delete=models.CASCADE, default=get_default_group)
    # group_id = models.ForeignKey(MyGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, null=True)
    availability = models.CharField(default='1900-2100', max_length=256)

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


class Feedback(Timestamp):
    remarks = models.CharField(max_length=200)
    receiver_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.remarks + " " + str(self.receiver_id)
        # return self.remarks


class Meeting(Timestamp):
    group_id = models.ForeignKey(MyGroup, on_delete=models.CASCADE)
    users = models.ManyToManyField(MyUser)
    url = models.CharField(max_length=200, default=False, blank=False)
    time = models.DateTimeField(auto_now=False)

    def __str__(self):
        return str(self.group_id) + " " + str(self.users) + " " + self.url + " " + str(self.time)
