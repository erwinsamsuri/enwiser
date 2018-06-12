# Generated by Django 2.0.6 on 2018-06-06 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20180605_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_checkoutlink',
            field=models.URLField(blank=True, default='#'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_content',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='product_img1',
            field=models.ImageField(default='DEFAULT VALUE', upload_to='imgs/products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_img2',
            field=models.ImageField(default='DEFAULT VALUE', upload_to='imgs/products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_img3',
            field=models.ImageField(default='DEFAULT VALUE', upload_to='imgs/products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_pricebefore',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_pricenow',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_pricetitle',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='product_tagline',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_sku',
            field=models.CharField(max_length=12),
        ),
    ]
