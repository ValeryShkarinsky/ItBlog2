from . import views
from django.urls import path

from .views import add_comment, delete_comment

urlpatterns = [path('glav/', views.mainblog, name='blog'),
               path('', views.article, name='stat'),
               path('detal/<int:pk>/', views.DetalView.as_view(), name='detal'),
               path('add_article/', views.add_article, name='add_article'),
               path('<int:pk>/update/', views.NewsUpdateView.as_view(), name='update_article'),
               path('<int:pk>/delete/', views.NewsDeleteView.as_view(), name='update_delete'),
               path('add_comment/<int:article_id>/', add_comment, name='add_comment'),
               path('delete_comment/<int:comment_id>/', delete_comment, name='delete_comment'),
               path('about/', views.about, name='about'),
               path('contact/', views.contact, name='contact'),
               ]