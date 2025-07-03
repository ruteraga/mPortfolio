from django.shortcuts import render, get_object_or_404
from .models import Project, Tag, ProjectImage
# Create your views here.

def home(request):
    return render(request, "index.html")

def project(request):
    projects=Project.objects.prefetch_related('images','tags').all()
    #tags = Tag.objects.all()
    #images=ProjectImage.objects.all()
    return render(request, "project.html", {"projects":projects}) 