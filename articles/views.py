from django.shortcuts import render
from .models import Article

def articles(request):
    return render(request, 'articles.html', { 'articles' : Article.objects.all() })

def article(request, pk):
    return render(request, 'article.html', { 'article' : Article.objects.get(pk = pk)} )