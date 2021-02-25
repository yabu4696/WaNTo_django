from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('rayout',views.rayout,name='rayout'),
    path('',  views.index, name='index'),
    path('item/<slug:slug>', views.detail, name='detail'),
    path('form', views.form, name='form'),
    path('delete', views.delete, name='delete'),
    path('reload',views.reload, name='reload'),
    path('item/<slug:slug>/edit', views.edit,name='edit'),
    path('item/<slug:slug>/exclusion', views.exclusion, name='exclusion'),
    path('maker_index',views.maker_index, name='maker_index'),
    path('maker/<slug:slug>', views.maker_detail, name='maker_detail'),
]