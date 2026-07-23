from django.contrib import admin
from blog.models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_date'
    empty_value_display = '-empty-'
    list_display = ('title','author','status','created_time')
    list_filter = ('status','author')
    search_fields = ['title']
    

admin.site.register(Post ,PostAdmin)