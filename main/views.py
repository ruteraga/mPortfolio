from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Project, Tag, ProjectImage, Post, Comment
from main.forms import CommentForm
# Create your views here.

def home(request):
    return render(request, "index.html")

def project(request):
    projects=Project.objects.prefetch_related('images','tags').all()
    #tags = Tag.objects.all()
    #images=ProjectImage.objects.all()
    return render(request, "project.html", {"projects":projects}) 



def blog(request):
    posts=Post.objects.all().order_by("-created_on")
    context={
        "posts":posts,
    }
    return render(request, "blog.html", context)

def blog_category(request, category):
    posts=Post.objects.filter(categories__name__contains=category).order_by("-created_on")

    context={
        "category":category,
        "posts":posts,
    }
    return render(request, "blog_category.html", context)


def blog_detail(request, pk):
    post=Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=Comment(
                author=form.cleaned_data["author"],
                email=form.cleaned_data["email"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
        
    comments=Comment.objects.filter(post=post)
    context={
        "post":post,
        "comments":comments,
        "form":CommentForm(),
    }

    return render(request, "blog_detail.html", context)