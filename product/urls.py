from django.urls import path
from django.shortcuts import render
from . import views
from django.urls import reverse, reverse_lazy, resolve

app_name = 'product'
urlpatterns = [
    # ex: /polls/
    path('', views.ProductListView.as_view(), name='product_list'),
 #   path('', views.index, name='index'),
    # ex: /polls/5/
#    path('<int:id>/', views.detail, name='product_detail'),

	path('<int:pk>/detail', views.ProductUpdateView.as_view(), name='product_change'),
	path('add/', views.ProductCreateNew.as_view(), name='product_create'),
#    path('add/', views.product_new, name='product_create'),
    # ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]