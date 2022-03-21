from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import StudentRegisterForm, TeacherRegisterForm 
from users.models import StudentInfo, DepartmentalHead, TeacherInfo, Profile
from django.views.decorators.csrf import csrf_protect
import random
import hashlib

def studentregister(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST,request.FILES)
        #print(form.errors)
        #print(form.is_valid())
        if form.is_valid():
            
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            
            full_name = request.POST['full_name']
            reg_no = request.POST['reg_no']
            dept = request.POST['dept']
            session = request.POST['session']
            
            email = request.POST['email']
            uploaded_image =form.cleaned_data.get("uploaded_image") #to get the data from forms!!!
            u_name = request.POST['username']
            password = request.POST['password2']
            p_hash = make_password(password)  ##to make hash password
            print(uploaded_image)
            userInfo = StudentInfo.objects.create(
                                 full_name=full_name, 
                                 reg_no=reg_no, 
                                 dept=dept, 
                                 session=session, 
                                 email=email, 
                                 role_id= 1, 
                                 uploaded_image = uploaded_image)
            #userInfo2 = User(username = u_name, email=email, password = p_hash)
            
            userInfo.save()
            #userInfo2.save()
            return redirect('login')
    else:
        form = StudentRegisterForm()
        
    return render(request, 'users/studentregister.html', {'form': form})

@csrf_protect
def teacherregister(request):
    if request.method == 'POST':
        form = TeacherRegisterForm(request.POST,request.FILES)
        if form.is_valid():
            print("hello")
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            
            full_name = request.POST['full_name']
            
            dept = request.POST['dept']
            
            email = request.POST['email']
            password = request.POST['password2']
            uploaded_image =form.cleaned_data.get("profile_picture")
            p_hash = make_password(password)  ##to make hash password
            print(p_hash)
            code = request.POST['code']
            u_name = request.POST['username']
            ans = 0
            assigned=TeacherInfo.objects.filter(code=code)
            a1 = DepartmentalHead.objects.all()
            for i in a1:
                if(i.code == code):
                    ans +=1
                    break
            print(ans)        

            print(len(assigned))
            #print(len(a1))
            
            if (len(assigned)==0 and (ans == 1)):
                #my_user = User.objects.create_user(username,email,password)
                
                #my_user = User(username = u_name, email=email, password = p_hash)
                #my_user.save()
                #print(my_user)
                form.save()
                
                userInfo = TeacherInfo.objects.create(full_name=full_name, 
                                                      dept=dept,  
                                                      email=email,
                                                      code=code, 
                                                      role_id = 2,
                                                      profile_picture = uploaded_image)
                userInfo.save()
                my_user = User.objects.get(username = u_name)
                departmentalHead=DepartmentalHead.objects.get(code=code)
                #print(departmentalHead)
                departmentalHead.user=my_user
                departmentalHead.save()


                #messages.add_message(request, messages.SUCCESS, 'Success!!')
                return redirect('login')

            else:
                #messages.add_message(request, messages.ERROR, 'Error!!')
                return redirect("http://127.0.0.1:8000/teacherregister")
    else:
        form = TeacherRegisterForm()
    return render(request, 'users/teacherregister.html', {'form': form})    


def intermediate(request):
    return render(request, 'users/intermediate.html')

@login_required
def profile(request):
    current_user = request.user
    
    score = Profile.objects.get(user = current_user)
    show = score.c_score
    print(show)
    #main_user_table = User.objects.all()
    obj1 = TeacherInfo.objects.all()
    obj2 = StudentInfo.objects.all()
    
    
    abcde = None

    for i in obj1:
        
        if (i.email == current_user.email):
            abcde = i
            break
    
    if(abcde==None):
        for i in obj2:
            
            if (i.email == current_user.email):
                abcde = i
                break
    cnt = 1
    ans = 0
    if abcde == None:
        cnt = 0
    else:
        ans = abcde.role_id

    #print(ans)
    ONE = str(1)
    #print(type(ONE))
    #print(type(abcde.role_id))
    TWO = 2
    if(current_user.is_superuser == False):
        
        context5 = abcde.uploaded_image.url

        return render(request, 'users/profile.html',{'context1':abcde, 'context2':cnt, 'context3':ans, 'context4':show, 'context5':context5})
    else:
        return render(request, 'users/profile.html',{'context1':abcde, 'context2':cnt, 'context3':ans, 'context4':show})




