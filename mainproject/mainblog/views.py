from django.shortcuts import render
from .models import Article



def mainblog(request):
    return render(request, 'blog.html')
def article(request):
    article = Article.objects.all()
    return render(request, 'article.html', {'article':article})