# Generated by Django 2.0.6 on 2018-06-06 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20180606_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_content',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_tagline',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
    ]