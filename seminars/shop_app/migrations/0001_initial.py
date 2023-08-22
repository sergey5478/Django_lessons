# Generated by Django 4.2.4 on 2023-08-22 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.TextField()),
                ('client_address', models.TextField()),
                ('customer_registration_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=100)),
                ('product_description', models.TextField()),
                ('price_product', models.TextField()),
                ('quantity_product', models.TextField()),
                ('date_product_added', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount_order', models.IntegerField()),
                ('date_order', models.DateTimeField(auto_now=True)),
                ('order_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_app.client')),
                ('order_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_app.product')),
            ],
        ),
    ]
