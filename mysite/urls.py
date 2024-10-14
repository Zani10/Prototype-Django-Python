from django.http import HttpResponse
from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'), 

    # Home and Article routes
    path('', views.article_list, name='article_list'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('fetch-images/', views.fetch_images, name='fetch_images'),
    
    # Profile route
    path('accounts/profile/', views.profile, name='profile'),
    
    # Article management routes
    path('add-article/', views.add_article, name='add_article'),
    path('article/<int:article_id>/edit/', views.edit_article, name='edit_article'),
    path('article/<int:article_id>/delete/', views.delete_article, name='delete_article'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
