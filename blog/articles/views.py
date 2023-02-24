from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.utils import timezone
#TODO
#ListView


def index(request):
    articles = Article.objects.order_by('publication_date')
    return render(request, 'articles/index.html', {'articles': articles, })


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article.html'
    context_object_name = 'article'


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'articles/article_update.html'
    fields = ['title', 'text', 'picture']


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = '/'
    template_name = 'articles/article_delete.html'


def about(request):
    return render(request, 'articles/about.html')


def contacts(request):
    return render(request, 'articles/contacts.html')


def article_create(request):
    error = ''

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.publication_date = timezone.now()
            post.save()
            return redirect('home')
        else:
            error = 'Возникла ошибка при обработке данных'

    form = ArticleForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'articles/article_creating.html', data)
