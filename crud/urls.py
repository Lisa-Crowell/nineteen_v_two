from django.urls import path
from . import views

urlpatterns = [
    path('', views.table, name='table'),
    path('create', views.create, name='create'),
    path('update/<int:pk>/', views.update_idea, name='update'),
    path('delete/<int:pk>/', views.delete_idea, name='delete')
]
