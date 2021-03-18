from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListDaily.as_view()),
    path('post/<int:pk>/', views.DetailDaily.as_view()),
    path('post/<str:cat>/', views.CategoryDairy.as_view()),
    path('contact/', views.ContactView.as_view()),
    path('ratio/', views.EvalRatio.as_view()),
    path('categories/', views.CategoryList.as_view())
]
