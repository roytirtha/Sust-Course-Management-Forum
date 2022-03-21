"""sust_course_management_forum_and_leaderboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from courses import views as course_views

from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('studentregister/', user_views.studentregister, name='studentregister'),
    path('teacherregister/', user_views.teacherregister, name='teacherregister'),
    path('int_register/', user_views.intermediate, name='int_register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('courses/', course_views.course_list, name='course_list'),
    path('courses/availableClasses/', course_views.showAvailableCourses, name='availableClasses'),
    path('courses/availableClasses/<str:c_name>', course_views.courseDetails, name='classNames'),
    path('courses/availableClasses/classname/createPost/sdk/sdk1/<str:s1>', course_views.createPost, name='createPost'),
    path('courses/availableClasses/course_add/course', course_views.courseadd, name='add_Course'),
    path('courses/availableClasses/sdk/sdk1/sdk2/<int:id>', course_views.commentView, name='createComment'),
    path('courses/availableClasses/sdk/sdk1/sdk2/sdk3/sdk4/<int:id>', course_views.increamentScore, name='score'),
    path('leaderboard/', course_views.leaderBoard, name='leaderBoard'),
    path('notification/', course_views.notifications, name='notifications'),
    path('', include('scmfal.urls')),
] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
