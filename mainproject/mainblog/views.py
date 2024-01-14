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
    success_url = reverse_lazy('/')
    template_name = 'delete.html'


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog.html')  # Перенаправление на страницу, где отображаются статьи
    else:
        form = ArticleForm()

    return render(request, 'add_article.html', {'form': form})


