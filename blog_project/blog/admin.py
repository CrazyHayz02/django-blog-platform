from django.contrib import admin
from .models import Post, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Columns displayed in list view
    list_display = ("title", "author", "created_at")
    
    # Add filters in admin sidebar
    list_filter = ("created_at", "author")
    
    # Search functionality
    search_fields = ("title", "content")
    
    # Default ordering
    ordering = ("-created_at",)

    # Only show posts the user owns, unless superuser
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    # Automatically assign logged-in user as author
    def save_model(self, request, obj, form, change):
        if not obj.author_id:  # if author not already set
            obj.author = request.user
        super().save_model(request, obj, form, change)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "created_at")
    list_filter = ("created_at",)
    search_fields = ("content",)

    # Only allow superusers to see all comments
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    # Assign logged-in user automatically
    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.site_header = "Blog Administration"
admin.site.site_title = "Blog Admin"
admin.site.index_title = "Welcome to Blog Admin"