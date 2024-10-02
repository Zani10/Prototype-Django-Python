from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm

# View for listing articles
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

# View for article detail
def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'article_detail.html', {'article': article})

@login_required
def profile(request):
    return render(request, 'profile.html')

def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user  # Assign the logged-in user as the author
            article.save()
            return redirect('article_list')  # Redirect to article list after saving
    else:
        form = ArticleForm()
    return render(request, 'add_article.html', {'form': form})