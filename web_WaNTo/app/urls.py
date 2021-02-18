from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('',  views.index, name='index'),
    path('<int:pk>/detail', views.detail, name='detail'),
    path('form', views.form, name='form'),
]