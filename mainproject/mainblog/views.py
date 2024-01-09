from django.shortcuts import render
from django.views.generic import DetailView
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

from .models import Article


def mainblog(request):
    return render(request, 'article.html')


def article(request):
    article = Article.objects.all()
    return render(request, 'blog.html', {'article': article})

class DetalVievs(DetailView):
    model = Article
    template_name = 'Detal.html'
    context_object_name = 'object'


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('article')  # Перенаправление на страницу, где отображаются статьи
    else:
        form = ArticleForm()

    return render(request, 'add_article.html', {'form': form})
