from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('',  views.index, name='index'),
    path('form', views.form, name='form'),
    path('delete', views.delete, name='delete'),
    path('reload',views.reload, name='reload'),
    path('<slug:slug>', views.detail, name='detail'),
    path('<slug:slug>/edit', views.edit,name='edit'),
    path('<slug:slug>/exclusion', views.exclusion, name='exclusion')
]