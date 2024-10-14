from django.contrib import admin
from .models import Article
from django import forms
from simple_history.admin import SimpleHistoryAdmin

class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 80}))

    class Meta:
        model = Article
        fields = '__all__'

# Admin with history
class ArticleAdmin(SimpleHistoryAdmin):  
    form = ArticleAdminForm
    list_display = ['title', 'author', 'created_at', 'updated_at']  
    history_list_display = ['title', 'author']  


admin.site.register(Article, ArticleAdmin)
