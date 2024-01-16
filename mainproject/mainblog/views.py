from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from .models import Article


def mainblog(request):
    return render(request, 'article.html')


def article(request):
    article = Article.objects.order_by('-date')
    return render(request, 'blog.html', {'article': article})

class DetalView(DetailView):
    model = Article
    template_name = 'Detal.html'
    context_object_name = 'object'

class NewsUpdateView(UpdateView):
    model = Article
    template_name = 'update.html'
    fields = ['title', 'anons', 'll_text']

class NewsDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog')
    template_name = 'delete.html'


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            # Дополнительные действия, если нужно
            article.save()
            return redirect('blog')  # Редирект, например, на главную страницу
    else:
        form = ArticleForm()  # Замените на вашу форму добавления статьи
    return render(request, 'add_article.html', {'form': form})

