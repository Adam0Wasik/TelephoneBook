from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('search', views.search),
    path('addNum/<int:osid>', views.addNumber),
    path('addEm/<int:osid>', views.addEmail),
    path('delete/<int:osid>', views.delete),
    path('edit/<int:osid>', views.edit),
]