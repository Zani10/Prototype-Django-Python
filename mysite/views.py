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
from django.conf import settings
from django.http import JsonResponse


# View for listing articles
def article_list(request):
    query = request.GET.get('q')
    if query:
        articles = Article.objects.filter(title__icontains=query) | Article.objects.filter(content__icontains=query)
    else:
        articles = Article.objects.all()

    paginator = Paginator(articles, 6)  # Show # articles per page
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
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            selected_image_url = request.POST.get('selected_image')
            if selected_image_url:
                article.image_url = selected_image_url 
            else:
                article.custom_image = request.FILES.get('custom_image') 
            article.save()
            messages.success(request, 'Your article has been created successfully!')
            return redirect('article_list')
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

# View for article history
@login_required
def article_history(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.user != article.author:
        return redirect('article_list')

    history = article.history.all() 
    return render(request, 'article_history.html', {'article': article, 'history': history})

# Restore a previous version of the article
@login_required
def restore_article(request, article_id, history_id):
    article = get_object_or_404(Article, pk=article_id)
    historical_article = article.history.filter(history_id=history_id).first()

    if not historical_article:
        messages.error(request, 'The requested version does not exist.')
        return redirect('article_history', article_id=article.id)

    article.title = historical_article.title
    article.content = historical_article.content
    article.save()

    messages.success(request, f'Restored to version from {historical_article.history_date}.')
    return redirect('article_detail', article_id=article.id)


@login_required
def preview_article(request, article_id, history_id):
    article = get_object_or_404(Article, pk=article_id)
    historical_article = article.history.filter(history_id=history_id).first()

    if not historical_article:
        messages.error(request, 'The requested version does not exist.')
        return redirect('article_history', article_id=article.id)

    return render(request, 'preview_article.html', {
        'article': historical_article,
    })


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


def fetch_images(request):
    query = request.GET.get('query', '')
    url = f"https://api.unsplash.com/search/photos?query={query}&client_id={settings.UNSPLASH_ACCESS_KEY}&per_page=10"
    response = requests.get(url)
    data = response.json()
    images = [{'url': image['urls']['small'], 'alt_description': image['alt_description']} for image in data['results']]
    return JsonResponse({'images': images})