from django import forms
from .models import Product

class ProductCreateForm(forms.ModelForm):
#	product_sku = forms.CharField(label='Your name')
 #   product_name = forms.CharField(label='Your name')

	product_sku = forms.CharField(max_length=40, 
		widget=forms.TextInput(
		attrs={'title': 'Your name', 'class' : 'form-control', 'placeholder' : 'Product SKU', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}))
	product_name = forms.CharField(max_length=40, 
		widget=forms.TextInput(
		attrs={'title': 'Your name', 'class' : 'form-control', 'placeholder' : 'Product SKU', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}))

	product_tagline = forms.CharField(max_length=40, 
			widget=forms.TextInput(
			attrs={'title': 'Your name', 'class' : 'form-control'}))

	product_content = forms.CharField(widget=forms.Textarea)
	product_pricetitle = forms.CharField(max_length=40, 
			widget=forms.TextInput(
			attrs={'title': 'Your name', 'class' : 'form-control'}))
	product_pricebefore = forms.IntegerField(
			widget=forms.TextInput(
			attrs={'class' : 'form-control'}))
	product_pricenow = forms.IntegerField(
			widget=forms.TextInput(
			attrs={'class' : 'form-control'}))
	product_checkoutlink = forms.URLField(max_length=40, 
			widget=forms.TextInput(
			attrs={'title': 'Your name', 'class' : 'form-control'}))
	product_img1 = forms.ImageField( required = False,
		widget=forms.ClearableFileInput(attrs={}))
	product_img2 = forms.ImageField( required = False,
		widget=forms.ClearableFileInput(attrs={}))
	product_img3 = forms.ImageField( required = False,
		widget=forms.ClearableFileInput(attrs={}))
	class Meta:
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