from . import views
from django.urls import path

urlpatterns = [path('glad/', views.mainblog, name='blog'),
               path('stat/', views.article, name='stat')]