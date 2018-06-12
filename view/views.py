import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from product.models import Product
# Create your views here.
def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def productview(request, p_id):
    product = get_object_or_404(Product, pk=p_id)
    return render(request, 'view/view.html', {'product': product})