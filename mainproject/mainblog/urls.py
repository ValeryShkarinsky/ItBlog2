from . import views
from django.urls import path

urlpatterns = [path('glav/', views.mainblog, name='blog'),
               path('', views.article, name='stat'),
               path('detal/<int:pk>/', views.DetalView.as_view(), name='detal'),
               path('add_article/', views.add_article, name='add_article'),
               path('<int:pk>/update/', views.NewsUpdateView.as_view(), name='update_article'),
               path('<int:pk>/delete/', views.NewsDeleteView.as_view(), name='update_delete')]