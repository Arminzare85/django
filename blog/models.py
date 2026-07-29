from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Post(models.Model):
    image = models.ImageField(upload_to='blog/' , default = 'blog/default.jpg')
    author = models.ForeignKey(User , on_delete=models.SET_NULL , null=True )
    title = models.CharField(max_length=250)
    content = models.TextField()
    # tags = 
    category = models.ManyToManyField(Category)
    counted_view = models.IntegerField(default = 0)
    status = models.BooleanField(default = False)
    published_date =models.DateTimeField(null = True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    class Meta:
        ordering =['-status']

    def __str__(self):
        return "{} - {}".format(self.title , self.id) 

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



