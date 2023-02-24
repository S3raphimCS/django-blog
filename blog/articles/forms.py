from .models import Article
from django import forms


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['author', 'picture', 'title', 'text']

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
