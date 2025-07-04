from django.shortcuts import render, get_object_or_404
from .models import Project, Tag, ProjectImage, Post, Comment
# Create your views here.

def home(request):
    return render(request, "index.html")

def project(request):
    projects=Project.objects.prefetch_related('images','tags').all()
    #tags = Tag.objects.all()
    #images=ProjectImage.objects.all()
    return render(request, "project.html", {"projects":projects}) 

def blog_category(request):
    posts=Post.objects.all().order_by("-created_on")
    context={
        "posts":posts,
    }
    return render(request, "blog_category.html", context)

def blog_detail(request, pk):
    post=Post.objects.get(pk=pk)
    comments=Comment.objects.filter(post=post)
    context={
        "post":post,
        "comments":comments,
    }

    return render(request, "blog_detail.html", context)