from django.contrib import admin
from .models import Article
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Article, ArticleAdmin)
