from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
#ListView


def index(request):
    articles = Article.objects.order_by('date')
    return render(request, 'articles/index.html', {'articles': articles, })


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article.html'
    context_object_name = 'article'


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
            post.date = timezone.now()
            post.save()
            # upload = request.FILES
            # fss = FileSystemStorage()
            # file = fss.save(upload.name, upload)
            # file_url = fss.url(file)
            # print(f'{upload}  | {file}  |  {file_url}')
            # with open(form.data['picture'], 'w') as f:
            #     f.write(str(settings.BASE_DIR) + r'\uploads')
            # form.save()
            return redirect('home')
        else:
            error = 'Возникла ошибка при обработке данных'

    form = ArticleForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'articles/article_creating.html', data)
