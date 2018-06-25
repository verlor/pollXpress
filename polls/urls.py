from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [

    path('', views.poll_index, name='polls'),

    path('manda', views.manda_la, name='manda_la')
]
