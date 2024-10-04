from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import CommentForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import SignUpForm


# View for listing articles
def article_list(request):
    query = request.GET.get('q')
    articles_list = Article.objects.all()

    if query:
        articles_list = articles_list.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    paginator = Paginator(articles_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'article_list.html', {'page_obj': page_obj, 'query': query})

# View for article detail
def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = article.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            return redirect('article_detail', article_id=article.id)
    else:
        form = CommentForm()
    return render(request, 'article_detail.html', {'article': article, 'comments': comments, 'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html')

# ADD
@login_required
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, 'Article created successfully!')
            return redirect('article_list')  # Redirect after saving
    else:
        form = ArticleForm()
    return render(request, 'add_article.html', {'form': form})

# EDIT 
@login_required
def edit_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.user != article.author:
        return redirect('article_list')  # Only the author can edit

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article updated successfully!')
            return redirect('article_detail', article_id=article.id)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'edit_article.html', {'form': form, 'article': article})

# DELETE
@login_required
def delete_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.user != article.author:
        return redirect('article_list')  # Only the author can delete

    if request.method == 'POST':
        article.delete()
        messages.success(request, 'Article deleted successfully!')
        return redirect('article_list')
    return render(request, 'delete_article.html', {'article': article})

@login_required
def profile(request):
    return render(request, 'profile.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('article_list')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
