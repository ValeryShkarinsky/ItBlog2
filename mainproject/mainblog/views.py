from django.shortcuts import render
from django.views.generic import DetailView

from .models import Article


def mainblog(request):
    return render(request, 'article.html')


def article(request):
    article = Article.objects.all()
    return render(request, 'blog.html', {'article': article})

class DetalVievs(DetailView):
    model = Article
    template_name = 'blog.html'
    context_object_name = 'object'


