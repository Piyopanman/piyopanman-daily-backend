from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('daily.urls')),
    path('markdownx/', include('markdownx.urls')),
]
