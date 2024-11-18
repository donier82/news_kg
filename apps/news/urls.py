from django.urls import path
from .views import NewsListCreate, NewsDetail

urlpatterns = [
    path('news/', NewsListCreate.as_view(), name='Список новостей'),  
    path('news/<int:pk>/', NewsDetail.as_view(), name='Детали новости'), 
]
