from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('daily/', include('daily.urls')),
    path('markdownx/', include('markdownx.urls')),
]
