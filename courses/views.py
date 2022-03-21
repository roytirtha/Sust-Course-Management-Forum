from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Courses, Post, Comments, LB
from .forms import CourseIncludeForm, PostForm, CommentForm
from users.models import StudentInfo, DepartmentalHead, Profile, TeacherInfo
from django.contrib.auth.models import User
from django.urls import reverse

def course_list(request):
    return render(request, 'courses/intermediate.html')

def showAvailableCourses(request):
    li1 = []
    li2 = []
    li1 =  Courses.objects.all()
    obj1 = TeacherInfo.objects.all()
    s1 = ""
    for i in li1:
        for j in obj1:
            if(i.teacher_name == j.full_name):
                
                li2.append(j.uploaded_image.url)
                break
       
        
        #obj1 = TeacherInfo.objects.get(full_name = 's1')
        #print(obj1.code)
    
    mylist = zip(li1, li2)

    c_user = request.user
    #print(c_user)
    
    ans = 0
    if (request.user.is_anonymous == False):
        print("Hello World")

        abcde = None

        for i in obj1:
        
            if (i.email == c_user.email):
                abcde = i
                
                break
        
        if (abcde== None):
            ans = 0
        else :
            ans = 1

    
        
    
    return render(request, 'courses/courselist.html', {'context': li1, "context1" : ans, 'context2':mylist})
    
def courseDetails(request, c_name):
    li1 = []
    li1 =  Courses.objects.get(course_name=c_name)
    
    
        
    context ={
            'course_name': li1.course_name,
            'course_code': li1.course_code,
            
            'course_description': li1.course_description,
            'teacher_name': li1.teacher_name
    }
    obj1 = Courses.objects.get(course_name = c_name)
    obj2 = obj1.id
    print(obj2)

    li2 = Post.objects.filter(course = obj2)
    li3 = []
    li4 = []
    li6 = User.objects.all()
    li7 = StudentInfo.objects.all()
    li8 = TeacherInfo.objects.all()
    print(li2)
    for k in li2:
       
        for j in li6:
            
            if(j==k.author):
                li3.append(j)
    
    for i in li3:
        for j in li7:
            if(i.email == j.email):
                li4.append(j.uploaded_image.url)   
    for i in li3:
        for j in li8:
            if(i.email == j.email):
                li4.append(j.uploaded_image.url)
    print(li4)            

    context2 = li2

    mylist = zip(li2, li4)
    
    
    return render(request, 'courses/course_details.html', {'context': context,'context2': context2, 'context3':mylist})

@login_required
def courseadd(request):
    if request.method == 'POST':
        form = CourseIncludeForm(request.POST)
        if form.is_valid():
            
           
            
            course_name = request.POST['course_name']
            course_code = request.POST['course_code']
            course_description = request.POST['course_description']
            #teacher_name = request.POST['teacher_name']
            #code = request.POST['code']
            current_user = request.user
            print(current_user.email)
            
            obj1 = TeacherInfo.objects.all()
          
            

            for i in obj1:
                if(i.email == current_user.email):  #iktu genjam
                    courseInfo = Courses(course_name=course_name, course_code=course_code, course_description=course_description, teacher_name = i.full_name, teacher = i)
                    courseInfo.save()
                    break
            return redirect('availableClasses')
   
    else:
        form = CourseIncludeForm()
    return render(request, 'courses/course_register.html', {'form': form})


@login_required
def createPost(request, s1):
    
    if request.method == 'POST':
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
            
           
           
            course =  Courses.objects.get(course_name=s1)
            c_id = course.id
            print(c_id)
            title = request.POST['title']
            body =  request.POST['body']
            #course = request.POST['course']
            #li1 =  Courses.objects.get(id=course)
            #c_name = li1.course_name
            author = request.user
            #current_user = request.user
            #print (current_user.id)
            #print (current_user.username)
            #author = instance.username
            uploaded_image =form.cleaned_data.get("add_image")
            singlePost = Post(title = title, body = body, author = author, course = course, add_image = uploaded_image)
            singlePost.user = request.user
            
            singlePost.save()

            return courseDetails(request, s1)

            
    else:
        form = PostForm()
    return render(request, 'courses/createPost.html', {'form': form})

@login_required
def commentView(request, id):
  
    if request.method == 'POST':
        cf = CommentForm(request.POST)
        if cf.is_valid():
            ID = id
            content = request.POST['content']
            post = Post.objects.get(id=id)
            comment = Comments.objects.create(post = post, author = request.user, body = content, score = 0)
            comment.save()
            
            s1 = "http://127.0.0.1:8000/courses/availableClasses/sdk/sdk1/sdk2/"
            print(s1+str(ID))
            return redirect(s1+str(ID))
    else:
        cf = CommentForm()

    li2 = Post.objects.get(id=id)
    context = li2

    obj1 = li2.author
    li3 = User.objects.all()
    li4= StudentInfo.objects.all()
    li5 = TeacherInfo.objects.all()
    li6=[]
    li7=[]
    for i in li3:
        if(i==obj1):
            li6.append(i)
            break
    
    for i in li6:
        for j in li4:

            if(i.email==j.email):
                li7.append(j)
                break
    for i in li6:
        for j in li5:

            if(i.email==j.email):
                li7.append(j)
                break
    
    mylist = li7[0].uploaded_image.url
    print(mylist)
    li8 = Comments.objects.filter(post = id)
    context3 = len(li8)
    context2 = li8
    li9 = []
    li10 = []
    for k in li8:
       
        for j in li3:
            
            if(j==k.author):
                li9.append(j)
    
    for i in li9:
        for j in li4:
            if(i.email == j.email):
                li10.append(j.uploaded_image.url)   
    for i in li9:
        for j in li5:
            if(i.email == j.email):
                li10.append(j.uploaded_image.url)
    mylist1 = zip(li8,li10)           

    
    return render(request, 'courses/createComment.html', {'form': cf, 'context':context, 'context2':context2, 'context3':context3, 'context4':mylist, 'context5':mylist1})  


def increamentScore(request, id):
    a1 = Comments.objects.get(id = id)
    b1 = a1.author 
    c1 = request.user
    
    

    if(b1!=c1 and (LB.objects.filter(comment = id, scorer = c1.id).exists())==False):
        obj1 = Comments.objects.get(id = id)
        obj1.score = obj1.score + 1
        obj1.save() #Update The Database
        obj34 = LB(comment = a1, scorer = c1)
        obj34.save()
    obj2 = a1.post
    

        

    

    return commentView(request, obj2.id) 

def leaderBoard(request):
    #obj1 = User.objects.all()
    obj2 = Comments.objects.all()
    obj1 = Profile.objects.all()

    
    '''for i in obj2:
        if(i.author == obj3.user)
       
        for j,k in zip(obj1, obj3):
            if(i.author == j ):
                if(k.user==j):
                    k.c_score = k.c_score + i.score
                    k.save()'''
               
    for i in obj1:
        sum = 0
        for j in obj2:
            if (j.author == i.user):
                
                sum+=j.score
        #i.c_score = i.c_score + j.score
        #i.save()
        i.c_score = sum
        i.save()
          
                        
    ordered_authors = Profile.objects.order_by('-c_score')[:5]
          
    cnt = 0
    for i in obj1:
        cnt+=1

                

    return render(request, 'courses/leaderboard.html',{'context':ordered_authors,'context1':"5"})

@login_required
def notifications(request):
    c_user = request.user
    obj1 = Post.objects.filter(author = c_user)
    print(obj1)
    ans = 0
    li1=[]
    li2 = []
    newlist = []
    if(obj1.exists()):
        
        
        for i in obj1:

            li2.append(i.id)
            obj2 = Comments.objects.filter(post = i)
            if(obj2.exists()):
                ans = 1
                for k in obj2:
                    li1.append(k)

        
                

    else:
        ans = 0            

    if(len(li1)>0):

        #print(li1.sort(key=lambda r: r.date_added))
        print(li1[0].date_added)
        # To sort the list in place...
        li1.sort(key=lambda x: x.date_added, reverse=True)

        # To return a new list, use the sorted() built-in function...
        newlist = sorted(li1, key=lambda x: x.date_added, reverse=True)

    
 
    
    return render(request, 'courses/notification.html', {'context1':newlist, 'context2':ans})



