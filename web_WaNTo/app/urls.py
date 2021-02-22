from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('',  views.index, name='index'),
    path('form', views.form, name='form'),
    path('delete', views.delete, name='delete'),
    path('reload',views.reload, name='reload'),
    path('<int:pk>/detail', views.detail, name='detail'),
    path('<int:pk>/detail/edit', views.edit,name='edit'),
    path('<int:pk>/detail/exclusion', views.exclusion, name='exclusion')
]