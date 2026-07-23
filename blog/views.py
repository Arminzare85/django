
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,JsonResponse
from blog.models import Post
from django.utils import timezone

def blog_view(request):
    posts = Post.objects.filter(status =1)
    context = {'posts': posts}
    return render(request ,'blog/blog-home.html',context)

def blog_single(request , pid):
    posts = list(Post.objects.filter(status =1))
    post = get_object_or_404( Post , id = pid)
    post_index = posts.index(post)
    if post_index>0:
        previous_post = posts[post_index - 1]
    else:
        previous_post = None
    if post_index < len(posts) - 1:
       next_post = posts[post_index + 1]
    else:
        next_post = None
    context = {'post': post,
               'previous_post': previous_post ,
               'next_post': next_post 
               }
    return render(request ,'blog/blog-single.html' , context)
def test(request,pid ):
    posts = get_object_or_404( Post ,id = pid)
    context = {'posts': posts}
    return render(request , 'test.html' , context)



