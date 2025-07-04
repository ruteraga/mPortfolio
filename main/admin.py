from django.contrib import admin
from .models import Tag, Project, ProjectImage, Category, Comment, Post
# Register your models here.
class ProjectImageInline(admin.TabularInline):
    model=ProjectImage
    extra=1

class ProjectAdmin(admin.ModelAdmin):
    list_display=("title","link")
    inlines=[ProjectImageInline]
    search_fileds=("title","description")
    list_filter=("tags",)

class TagAdmin(admin.ModelAdmin):
    list_display=("name",)
    search_fields=("name",)

class Projectdatas(admin.ModelAdmin):
    list_display=("name",)
    search_fields=("name",)

class CategoryAdmin(admin.ModelAdmin):
    pass
class PostAdmin(admin.ModelAdmin):
    pass
class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
