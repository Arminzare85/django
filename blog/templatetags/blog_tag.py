from django import template
from blog.models import Post , Category

register = template.Library()



@register.filter
def snippet(value , arg):
    return value[:arg]+"..."

@register.inclusion_tag("blog/blog-popular.html")
def popularposts():
    posts = Post.objects.filter(status=1).order_by("published_date")[:3]
    return {"posts":posts}
    
@register.inclusion_tag("blog/blog-ads.html")
def ads():  
    return {}
@register.inclusion_tag("blog/blog-writer.html")
def writer():
    return {}
@register.inclusion_tag("blog/blog-category.html")
def category():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict ={}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {"categories":cat_dict}