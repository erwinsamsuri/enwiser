from django.db import models
from django.urls import reverse, reverse_lazy, resolve
import os, random, uuid
import datetime


# Create your models here.
def content_file_name(instance, filename):
    rand = random.randint(10000,999999)
    ext = ".png"
    time = datetime.datetime.now()
    newname = "enwiser_%d%d8%s%s" % (time.month, time.day, rand, ext)
    return os.path.join('imgs/products/', newname)

class Product(models.Model):
	product_sku = models.CharField(max_length=12)
	product_name = models.CharField(max_length=255)
	product_tagline = models.CharField(blank=True, max_length=400, default='')
	product_content = models.TextField(blank=True, max_length=2000, default='')
	product_pricetitle = models.CharField(max_length=255, default='')
	product_pricebefore = models.IntegerField(default='0')
	product_pricenow = models.IntegerField(default='0')
	product_checkoutlink = models.URLField(blank=True, default='#')
	product_img1 = models.ImageField(null = True, blank = True, upload_to=content_file_name, default='')
	product_img2 = models.ImageField(null = True, blank = True, upload_to=content_file_name, default='')
	product_img3 = models.ImageField(null = True, blank = True, upload_to=content_file_name, default='')
	def get_absolute_url(self):
		return reverse('product:product_list')

