from django.urls import path
from . import views
from blog.views import PostDetail, Archive, Posts


urlpatterns = [
    path('', Posts, name="home"),
    path('<slug:slug>', PostDetail, name="post_detail"),
    path('blog/archive/', Archive.as_view(), name="archive" ),
]