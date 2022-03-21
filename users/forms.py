from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from .models import TeacherInfo

username_validator = UnicodeUsernameValidator()


class StudentRegisterForm(UserCreationForm):
    
    full_name = forms.CharField(label=('Name'), max_length=100, min_length=4, required=True, 
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    reg_no = forms.CharField(
        label = ('Registration Number'),
        min_length=10,
        max_length=10,
        
        error_messages={'unique': _("Please correctly enter you reg_no.")},
        widget=forms.TextInput(attrs={'class': 'form-control', 'type':'number'}),
        #blank = True
    )
    dept = forms.CharField(
        label = ('Department'),
        min_length=3,
        max_length=3,
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    session = forms.CharField(
        label = ('Session'),
        min_length=5,
        max_length=5,
        
        widget=forms.TextInput(attrs={'class': 'form-control'}))

         

    email = forms.EmailField(max_length=50, help_text='Required a valid email address.',
                             widget=(forms.TextInput(attrs={'class': 'form-control'})))
    password1 = forms.CharField(label=_('Password'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control'})),
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=_('Password Confirmation'), widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                )
    username = forms.CharField(
        label=_('Username'),
        max_length=150,
        help_text=_('Required 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={'unique': _("A user with that username already exists.")},
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    uploaded_image = forms.ImageField()

    class Meta:
        model = User
        fields = ('full_name', 'dept', 'email', 'reg_no', 'session', 'username', 'password1', 'password2', 'uploaded_image')

class TeacherRegisterForm(UserCreationForm):
    
    full_name = forms.CharField(label=('Name'), max_length=100, min_length=4, required=True, 
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    
    dept = forms.CharField(
        label = ('Department'),
        min_length=3,
        max_length=3,
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    
    email = forms.EmailField(max_length=50, help_text='Required a valid email address.',
                             widget=(forms.TextInput(attrs={'class': 'form-control'})))

    code = forms.CharField(max_length=10,
                             widget=(forms.TextInput(attrs={'class': 'form-control'})))                      
    password1 = forms.CharField(label=_('Password'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control'})),
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=_('Password Confirmation'), widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                )
    username = forms.CharField(
        label=_('Username'),
        max_length=150,
        help_text=_('Required 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={'unique': _("A user with that username already exists.")},
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    profile_picture = forms.ImageField()

    class Meta:
        model = User
        fields = ('full_name', 'dept', 'email', 'code','username', 'password1', 'password2', 'profile_picture')

   
   
   
    ##code = forms.CharField(max_length=10,widget=(forms.TextInput(attrs={'class':'form-control'}))),    