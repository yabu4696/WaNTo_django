from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', admin.site.urls),
    # path('wanto', include('wantem.urls')),
    # path('home', include('home.urls')),
]
