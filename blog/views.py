
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,JsonResponse
from blog.models import Post 
from blog.forms import CommentForm 
from django.contrib import messages

from django.utils import timezone
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger

def blog_view(request,cat_name=None,author_username=None,page_num=1):
    posts = Post.objects.filter(
    status=True,
    published_date__lte=timezone.now()
)
    
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if author_username:
        posts = posts.filter(author__username=author_username)   

    posts = Paginator(posts,3)
   
    posts=posts.get_page(page_num)     
    context = {'posts': posts}
    print(author_username)
    return render(request ,'blog/blog-home.html',context)
def blog_single(request , pid):
    posts = list(Post.objects.filter(status =1))

    post = get_object_or_404( Post , id = pid ,published_date__lte=timezone.now()) 
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        # comment.name = "unknown"
        comment.save()
        messages.success(request, "successfully posted")
        return redirect('blog:single', pid=post.id)
    post.counted_view += 1
    post.save()
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
               'next_post': next_post ,
               "form": form,
               }
    return render(request ,'blog/blog-single.html' , context)
# def test(request,pid ):
#     posts = get_object_or_404( Post ,id = pid)
#     context = {'posts': posts}
#     return render(request , 'test.html' , context)
def blog_category(request,cat_name):
    posts = Post.objects.filter(status =1)
    posts=posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request ,'blog/blog-home.html' , context)

def blog_search(request):
    posts = Post.objects.filter(status =1)
    search = request.GET.get("s")

    if search:
        posts = posts.filter(content__icontains=search)
    context = {'posts': posts}
    return render(request ,'blog/blog-home.html',context)

    





