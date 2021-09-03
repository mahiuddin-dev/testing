from django.contrib import admin
from .models import Post, Comment, Category

# Register your models here

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display= [
        'name',
        'slug'
    ]
    prepopulated_fields={
        'slug':('name',)
    }

class PostAdmin(admin.ModelAdmin):
    list_display=[ 
        'title',
        'thumbnail',
        'description'
    ]

admin.site.register(Post,PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    
    list_display = [
        'name',
        'body'
      
    ]

admin.site.register(Comment, CommentAdmin)

