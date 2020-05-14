from django.views import generic
from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Flatpage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext

# Create your views here.
# class PostList(generic.TemplateView):
#     posts = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'blog/index.html'

def Posts(request):
    flatpage = Flatpage.objects.get(pk=1)
    posts = Post.objects.filter(status=1).order_by('-created_on')[:8]
    return render(request, 'blog/index.html', {'posts': posts, 'flatpage': flatpage})

# class Posts(ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')[:4]
#     context_object_name = 'posts'
#     template_name = 'blog/index.html'

def PostDetail(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    return render(request, template_name, {'post': post })

# def Archive(request):
#     paginate_by = 2
#     model = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'blog/archive.html'
#     return render(request, template_name, {'posts': model })

class Archive(ListView):
    model = Post
    template_name = 'blog/archive.html'
    context_object_name = 'posts'  
    paginate_by = 4
    queryset = Post.objects.filter(status=1).order_by('-created_on')


