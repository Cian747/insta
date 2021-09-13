from django.forms import widgets
from gram.models import Image
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Image,Comment,Profile


class InstaRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username','password1','password2' ]

        widgets = {
            'first_name':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"First Name", 'label': 'First Name'}),
            'last_name':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Second Name", 'label': 'Second Name'}),
            'email':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Email Address", 'label': 'Email Address'}),
            'username':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Username", 'label': 'Username'}),
            'password1':forms.PasswordInput(attrs = {'class':'form-control ','type':'password', 'placeholder':"Password", 'label': 'Password'}),
            'password2':forms.PasswordInput(attrs = {'class':'form-control', 'placeholder':"Confirm Password", 'label': 'Confirm Password'}),
        }

class PostImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image','image_name','image_caption','profile']

        widgets = {
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'image_name':forms.TextInput(attrs={'class':'form-control names','placeholder':'In a word...','label':'Put a name'}),
            'image_caption':forms.Textarea(attrs={'class':'form-control names','placeholder':"Caption",'label':"Caption"}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

        widgets = {
            'comment': forms.TextInput(attrs={'class':'form-control','name':'comment'})
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo','bio']

        widgets = {
            'profile_photo':forms.FileInput(attrs={'class':'form-control'}),
            'bio':forms.Textarea(attrs={'class':'form-control names','placeholder':'Write here...','label':'Put a name'}),
        }