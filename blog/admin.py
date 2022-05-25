from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    # Display the properties
    list_display = ('title', 'slug', 'status', 'created_on')
    # Filter the post based on the status
    list_filter = ('status',)
    # Search the database from the search_fields attributes
    search_fields = ['title', 'content']
    # Prepopulate slug field from title field
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
