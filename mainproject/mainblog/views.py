from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from .models import Article
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment
from .forms import CommentForm


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
    success_url = reverse_lazy('stat')
    template_name = 'delete.html'



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article


@login_required(login_url='login')
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('stat')
    else:
        form = ArticleForm()

    return render(request, 'add_article.html', {'form': form})


# views.py



def add_comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect('article_detail', pk=article.id)
    else:
        form = CommentForm()

    return render(request, 'add_comment.html', {'form': form})


