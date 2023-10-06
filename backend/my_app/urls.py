from django.urls import path
from . import views


urlpatterns = [
    path('', views.create_publication_view, name='create_publication'),
    path('detail/<int:pk>/', views.publication_detail_view, name='publication_detail'),
    path('form/', views.my_view, name='form'),
    path('result/', views.result_view, name='result'),
]
