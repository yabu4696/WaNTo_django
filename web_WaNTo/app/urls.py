from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('',  views.index, name='index'),
    path('<int:pk>/detail', views.detail, name='detail'),
    path('form', views.form, name='form'),
    path('delete', views.delete, name='delete'),
    path('<int:pk>/reload',views.reload, name='reload'),
    path('<int:pk>/exclusion', views.exclusion, name='exclusion')
]