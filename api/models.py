from django.db import models
from django.contrib.auth.models import User, Group, AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
# class User(AbstractUser):
#     is_student = models.BooleanField('student status', default=False)
#     is_teacher = models.BooleanField('teacher status', default=False)

# class Feedback(models.Model):

class Meeting(models.Model):
    #groupid = models.ForeignKey(Group, on_delete=models.CASCADE)
    user=models.ManyToManyField(User)
    meeting_Url=models.CharField(max_length=200,default=False,blank=False)
    meeting_Time=models.DateTimeField(auto_now=False)

    
