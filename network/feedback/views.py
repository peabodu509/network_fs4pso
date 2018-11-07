from __future__ import unicode_literals
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.template import RequestContext
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import PostForm, CommentForm, LoginForm, SignUpForm
from .models import Post, Subject, Comment, Like

def allPosts(request):
    subjects = Subject.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date').reverse()
    return render(request, 'posts.html', {'subjects': subjects, 'posts': posts})

def sortedPosts(request, subject_id):
    subjects = Subject.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    posts = Post.objects.filter(created_date__lte=timezone.now(), subject = subject_id).order_by('created_date').reverse()
    return render(request, 'posts.html', {'subjects': subjects, 'posts': posts})

def likes(request, post_id):
    post = Post.objects.get(id = post_id)
    new_like, created = Like.objects.get_or_create(user=request.user, post_id=post_id)
    if not created:
        post.numOfLike -= 1
        like = Like.objects.get(user=request.user, post_id=post_id)
        like.delete()
        created = True
    else:
        post.numOfLike += 1
    post.save(update_fields=['numOfLike'])
    return HttpResponseRedirect("/")

def detail(request, post_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(id = post_id)
            comment.user = request.user
            comment.created_date = timezone.now()
            comment.save()
            return redirect('/detail/{}'.format(post_id))
    else:
        form = CommentForm()
    subjects = Subject.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    posts = Post.objects.filter(id = post_id)
    comments = Comment.objects.filter(post = post_id).order_by('created_date').reverse()
    return render(request, 'detail.html', {'posts':posts, 'subjects':subjects, 'comments':comments, 'form':form})

def write(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('allPosts')
    else:
        form = PostForm()
    subjects = Subject.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'write.html', {'form': form, 'subjects': subjects})

def terms(request):
    subjects = Subject.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'terms.html', {'subjects': subjects})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, pasword=raw_password)
            return redirect('/accounts/login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})

def passwordReset(request):
    subjects = Subject.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'find.html', {'subjects': subjects})