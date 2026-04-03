from django.urls import path
from . import views

urlpatterns = [
    path('', views.player_list, name='player_list'),
    path('add/', views.player_create, name='player_add'),
    path('view/<int:pk>/', views.player_detail, name='player_detail'),
    path('edit/<int:pk>/', views.player_update, name='player_edit'),
    path('delete/<int:pk>/', views.player_delete, name='player_delete'),
]
