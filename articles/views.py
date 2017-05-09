from django.shortcuts import render, redirect
from .models import Article, Comment
from forms import CommentForm
from django.template.context_processors import csrf
from django.utils import timezone
from django.template.defaulttags import comment

def articles(request):
    return render(request, 'articles.html', { 'articles' : Article.objects.all() })

def article(request, pk):
    return render(request, 'article.html', { 'article' : Article.objects.get(pk = pk)} )

def add_comment(request, pk):
    art = Article.objects.get(pk = pk)
    
    if request.method == "POST":
        cf = CommentForm(request.POST)
        if cf.is_valid():
            comment = cf.save(commit = False)
            comment.published = timezone.now()
            comment.article = art
            comment.save()
            
            return redirect('article', pk=art.pk)
    else:
        cf = CommentForm()
        
    args = {}
    args.update(csrf(request))
    args['article'] = art
    args['form'] = cf
    
    return render(request, 'add_comment.html/', args)

