from django.urls import path

from . import views

app_name = 'view'
urlpatterns = [
	path('', views.index, name='index'),
	path('<p_id>/', views.productview, name='product_change'),
	]