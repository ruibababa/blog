"""srblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogweb import views
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('message/', views.get_message, name='get_message'),
    path('form/', views.get_content, name='get_content'),
    path('home/', views.home, name='home'),
    path('articles/<int:id>/', views.detail, name='detail'),
    path('summernote/', include('django_summernote.urls')),
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('category/<int:id>/', views.search_category, name='category_menu'),
    path('tag/<str:tag>/', views.search_tag, name='search_tag'),


]
