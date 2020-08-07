from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_messages', views.get_messages, name='get_messages'),
]