from django.urls import path
from . import views

urlpatterns=[
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("project/",views.project, name="project"),
    path("blog/", views.blog, name="blog"),
    path("post/<int:pk>/",views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category")
    #path("home/", views.home, name="home"),
    #path("contact/", views.contact, name="contact"),
    #path("project/<int:id>/", views.project, name="project")
]