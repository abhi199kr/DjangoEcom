from django.contrib import admin

# Register your models here.
from bloghome.models import Blog
class BlogAdmin(admin.ModelAdmin):
    class Media:
        css={
            "all":("css/main.css",)
        }
    
        js=("js/blog.js",)
    
admin.site.register(Blog,BlogAdmin)