from django.db import models

class Post(models.Model):
    # image =
    # author = 
    title = models.CharField(max_length=250)
    content = models.TextField()
    # tags = 
    # category = 
    counted_view = models.IntegerField(default = 0)
    status = models.BooleanField(default = False)
    published_date =models.DateTimeField(null = True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.title , self.id)


