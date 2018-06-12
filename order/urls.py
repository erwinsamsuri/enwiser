from django.urls import path

from . import views

app_name = 'order'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.order_new, name='order_new'),
    path('<int:pk>/detail', views.order_new, name='order_detail'),
]