from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from .models import *
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def poll_index(request):
    form = ArticleForm()
    return render(request, 'polls/encuesta.html', {
    'form': form
    })

def manda_la(request):
    f = ArticleForm(request.POST)
    articulo = f.save(commit=False)
    articulo.pub_date = timezone.now()

    articulo.save()

    return render(request, 'polls/encuesta.html', {
    'form': ArticleForm(),
    'myValue' : 1
    })
