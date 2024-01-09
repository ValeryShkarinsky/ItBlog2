from . import views
from django.urls import path

urlpatterns = [path('glav/', views.mainblog, name='blog'),
               path('', views.article, name='stat'),
               path('detal/<int:pk>/', views.DetalVievs.as_view(), name='detal'),
               path('add_article/', views.add_article, name='add_article')]