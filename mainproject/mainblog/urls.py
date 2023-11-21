from . import views
from django.urls import path

urlpatterns = [path('Blog/', views.mainblog, name='blog'),
               path('Stat/', views.article, name='stat')]