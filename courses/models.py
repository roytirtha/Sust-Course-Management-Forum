from django.db import models
from django.contrib.auth.models import User
from users.models import TeacherInfo
class Courses(models.Model):
    course_name = models.CharField(max_length=120)
    course_code = models.CharField(max_length=6)
    course_description = models.CharField(max_length = 500)
    teacher_name = models.CharField(max_length=120)
    teacher = models.ForeignKey(TeacherInfo,on_delete=models.CASCADE,blank=True,null=True)
    #code = models.CharField(max_length=10)

    def __str__(self):
        return '%s' %(self.course_name)




class Post(models.Model):
    title =  models.CharField(max_length=1000)
    course = models.ForeignKey(Courses,on_delete=models.CASCADE,blank=True,null=True) #Foreign Key
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True) #Foreign Key
    body = models.TextField(null = True, blank = True)
    post_date = models.DateTimeField(auto_now_add = True)
    add_image = models.ImageField(null = True, blank = True, upload_to = "images/")

    def __str__(self):
        return '%s' %(self.title)

class Comments(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,blank=True,null=True) #Foreign Key
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True) #Foreign Key
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True) 
    score = models.IntegerField()

    def __str__(self):
        return '%s' %(self.body)

class LB(models.Model):
    comment =  models.ForeignKey(Comments,on_delete=models.CASCADE,blank=True,null=True) #Foreign Key
    scorer = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True) #Foreign Key
   
    def __str__(self):
        return '%s' %(self.scorer)        
