from django.db import models

# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name
class Project(models.Model):
    title= models.CharField(max_length=200)
    description=models.TextField()
    tags=models.ManyToManyField(Tag, related_name="projects")
    link=models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title
    
class ProjectImage(models.Model):
    project=models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE)
    image=models.ImageField(upload_to="project_images/")

    def __str__(self):
        return f"{self.project.title} Image"

class Category(models.Model):
    name=models.CharField(max_length=30)

    class Meta:
        verbose_name_plural="categories"
    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=30)
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    last_modified=models.DateTimeField(auto_now=True)
    categories=models.ManyToManyField("Category", related_name="posts")

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    author=models.CharField(max_length=60)
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"
