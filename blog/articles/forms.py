from .models import Article
from django import forms

# Не работает добавление картинки при создании статьи через create (form)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['author', 'picture', 'title', 'text', 'date']

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название статьи",
            }),
            "picture": forms.FileInput(attrs={
                "class": "form-control",
                "name": "image",
                "placeholder": "Картинка для статьи",
                "accept": ".jpg, .png"
            }),
            "text": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Основной текст статьи",
            }),
        }
