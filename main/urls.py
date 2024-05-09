from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('apartments/', views.apartments, name='apartments'),
    path('post/', views.post_application, name='post'),
    path('apartments/<int:id>/', views.detail, name='detail'),
]