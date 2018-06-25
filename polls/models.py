from django.db import models
from django.forms import ModelForm, Textarea
from django import forms
# Create your models here.

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateTimeField('publicado')

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        exclude = ('pub_date',)
        widgets = {
            'headline': Textarea(attrs={'ng-hide':"checked"}),
        }
