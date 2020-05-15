from django.urls import path
from .views import *

urlpatterns = [
    path('', ArticlesView.as_view(), name='articles'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='post_detail'),
]