from django.contrib import admin
from .models import Article  # Import the Article model

# Register the Article model to make it appear in the admin panel
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
