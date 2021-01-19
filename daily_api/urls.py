from django.contrib import admin
from django.urls import path, include

admin.site.site_title = "ぴよぱんまんのサイト"
admin.site.site_header = "ぴよぱんまんのサイト"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('daily/', include('daily.urls')),
    path('markdownx/', include('markdownx.urls')),
]
