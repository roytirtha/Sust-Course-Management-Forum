from django.contrib import admin
from users.models import StudentInfo, DepartmentalHead, Profile, TeacherInfo




admin.site.site_header= 'Departmental Head Dashboard'






admin.site.register(StudentInfo)
admin.site.register(TeacherInfo)
admin.site.register(DepartmentalHead)
admin.site.register(Profile)