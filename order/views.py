from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def index(request):
    return render(request, 'order/order_list.html', {})

def order_new(request):
    return render(request, 'order/order_detail.html', {})

def order_detail(request, id):
    return render(request, 'order/order_detail.html', {})