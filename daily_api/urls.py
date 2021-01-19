from django.contrib import admin
from django.urls import path, include

admin.site.site_title = "ぴよぱんまん ∧( 'Θ' )∧"
admin.site.site_header = "ぴよぱんまん ∧( 'Θ' )∧"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('daily/', include('daily.urls')),
    path('markdownx/', include('markdownx.urls')),
]
