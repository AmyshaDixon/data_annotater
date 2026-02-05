from django.urls import path
from . import views

urlpatterns = [
    path('', views.annotation_list, name = 'annotation_list'),
    path('upload/', views.upload_csv, name = 'upload_csv'),
    path('edit/<int:id>/', views.edit_annotation, name = 'edit_annotation'),
]