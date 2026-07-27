from django import template
from blog.models import Post , Category

register = template.Library()
@register.inclusion_tag("website/latest.html")
def latest():
    posts = Post.objects.filter(status=True).order_by("-published_date")
    return {
        "posts": posts
    }

@register.filter
def snippet(value , arg):
    return value[:arg]+"..."