from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .forms import ProductCreateForm
from  django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.template import loader
from .models import Product
import datetime
# Create your views here.
def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return redirect('product:product_change', pk=product.pk)
#    return render(request, 'product/detail.html', {'product': product})

def product_new(request): #product_add.html
    if request.method == "POST":
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('product:product_change', pk=product.pk)
    else:
        form = ProductCreateForm()
    return render(request, 'product/product_add.html', {'form': form})

class ProductCreateNew(CreateView):
    model = Product
    fields = (
        'product_sku', 
        'product_name',
        'product_tagline',
        'product_content',
        'product_pricetitle',
        'product_pricebefore',
        'product_pricenow',
        'product_checkoutlink',
        'product_img1',
        'product_img2',
        'product_img3',
        )
    template_name = 'product/product_form.html'

class ProductUpdateView(UpdateView): #product_form.html
    model = Product
    fields = (
        'product_sku', 
        'product_name',
        'product_tagline',
        'product_content',
        'product_pricetitle',
        'product_pricebefore',
        'product_pricenow',
        'product_checkoutlink',
        'product_img1',
        'product_img2',
        'product_img3',
        )
    template_name = 'product/product_form.html'

class ProductListView(ListView):
    model = Product
    context_object_name = 'product_list'

