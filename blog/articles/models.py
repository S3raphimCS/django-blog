from django.db import models
from django.utils import timezone

# Create your models here.


class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    picture = models.ImageField('Картинка', default='NULL', upload_to='uploads')
    title = models.CharField('Название', max_length=50)
    text = models.TextField('Текст статьи')
    publication_date = models.DateTimeField('Дата публикации', auto_now_add=True, blank=True)
    date_of_last_change = models.DateTimeField('Дата последнего изменения', auto_now=True)

    def __str__(self):
        return f'Статья: {self.title}'

    def get_absolute_url(self):
        return f'/article-{self.id}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
