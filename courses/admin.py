from django.contrib import admin
from courses.models import Courses, Post, Comments, LB
# Register your models here.
admin.site.register(Courses)
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(LB)