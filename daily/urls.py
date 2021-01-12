from django.urls import path
from . import views

# localhost:8000/api/のあとの話
urlpatterns = [
    path('', views.ListDaily.as_view()),
    path('<int:pk>/', views.DetailDaily.as_view()),
    path('<str:cat>/', views.CategoryDairy.as_view()),
    path('contact/', views.Contact.as_view()),
]
