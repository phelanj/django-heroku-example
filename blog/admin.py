from django.contrib import admin
from .models import Post, Flatpage

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on',)
    list_filter = ("status",)
    search_fields = ['title', 'content', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    view_on_site = True


class FlatpageAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')

    
admin.site.register(Flatpage, FlatpageAdmin)
admin.site.register(Post, PostAdmin)
