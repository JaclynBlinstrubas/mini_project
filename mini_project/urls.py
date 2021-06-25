from django.urls import path
from rest_framework import urlpatterns
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('cats/', views.CatList.as_view(), name='cat_list'),
    path('cats/<int:pk>', views.ListDetail.as_view(), name='cat_detail'),
    path('comments/', views.CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name='comment_detail')
]