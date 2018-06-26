from django.db import models
from django.forms import ModelForm, Textarea
from django import forms
# Create your models here.

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateTimeField('publicado')
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )


    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        exclude = ('pub_date',)
        
