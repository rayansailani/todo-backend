from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverView, name="overview"),
    path('tasks', views.taskList, name="taskList"),
    path('task/<str:pk>/', views.detailView, name="detailView"),
    path('create/', views.createView, name = 'createView'),
    path('update/<str:pk>/', views.updateView, name = 'updateView'),
    path('delete/<str:pk>/', views.deleteView, name="deleteView"),
]
