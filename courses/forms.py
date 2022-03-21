from django import forms
from .models import Courses, Post, Comments
class CourseIncludeForm(forms.ModelForm):
    course_name = forms.CharField(label='Course Name', max_length=100)
    course_code = forms.CharField(label='Course Code', max_length=100)
    course_description = forms.CharField(label='Course Description', max_length=500)
    #teacher_name = forms.CharField(label='Teacher Name', max_length=100)
    #code = forms.CharField(label='Code', max_length=10)
    class Meta:
        model = Courses
        fields = ('course_name', 'course_code', 'course_description')

class PostForm(forms.ModelForm):
    
    title = forms.CharField(label='Title', max_length=100)
    #author = forms.CharField(label='Author', max_length=100)
    body = forms.CharField(label='Post', widget=forms.Textarea)
    add_image = forms.ImageField(required=False)
    
    class Meta:
        model = Post
        fields = ('title', 'body', 'add_image')
        
       

class CommentForm(forms.ModelForm):
    content = forms.CharField(label ="", widget = forms.Textarea(
    attrs ={
        #'class':'form-control',
        'placeholder':'Comment here !',
        'rows':'5',
        'cols':'100'
    }))
    
    class Meta:
        model = Comments
        fields =['content']       

