from django.db import models
import random
from django.db.models.signals import pre_save
from .utils import random_string_generator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class StudentInfo(models.Model):
    full_name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=10)
    dept = models.CharField(max_length=3)
    session = models.CharField(max_length=5)
    role_id = models.CharField(max_length=1)
    email = models.EmailField()
    uploaded_image = models.ImageField(null = True, blank = True, upload_to = "images/")

    def __str__(self):
        return '%s' %(self.full_name)

class TeacherInfo(models.Model):
   full_name = models.CharField(max_length=100)
   
   dept = models.CharField(max_length=3)
   code = models.CharField(max_length=10)
   email = models.EmailField()
   role_id = models.CharField(max_length=1)
   uploaded_image = models.ImageField(null = True, blank = True, upload_to = "images/")
   #u_name = models.CharField(max_length=20)
   def __str__(self):
        return '%s' %(self.full_name)


      

class DepartmentalHead(models.Model):
     code = models.CharField(max_length=10,null=True,blank=True)
     user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.code:
        instance.code =random_string_generator(size=6)

pre_save.connect(pre_save_receiver, sender=DepartmentalHead)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    c_score = models.IntegerField(null=True) 

    def __str__(self):
        return '%s' %(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()         
     
    