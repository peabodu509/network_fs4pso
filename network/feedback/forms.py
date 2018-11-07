from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('subject', 'goodPoint', 'improvingPoint', 'anotherPoint',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('commentDesc',)

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='선택사항입니다.')
    last_name = forms.CharField(max_length=30, required=False, help_text='선택사항입니다.')
    email = forms.EmailField(max_length=254, help_text = '비밀번호 찾기에 사용되므로 유효한 이메일 주소를 입력하여 주십시오.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)