from django.urls import path, include
from . import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('list/article/', views.ArticleList.as_view(), name='article-list'),
    path('list/article/<int:pk>/', views.ArticleEdit.as_view(), name='article-rud'),
]
