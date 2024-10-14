from django.contrib import admin
from .models import Article
from django import forms


class ArticleAdminForm(forms.ModelForm):
   
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 80}))

    class Meta:
        model = Article
        fields = '__all__'

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm


admin.site.register(Article, ArticleAdmin)
