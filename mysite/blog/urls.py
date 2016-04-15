from blog.models import Post
from django.conf.urls import url
from django.views.generic import ListView

urlpatterns = [
    url(r'^$', ListView.as_view(
        queryset=Post.objects.all().order_by("-date")[:25],
        template_name="blog/blog.html")),
]
