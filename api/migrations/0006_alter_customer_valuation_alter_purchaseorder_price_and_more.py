# Generated by Django 4.1.3 on 2022-11-19 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_customer_valuation_alter_purchaseorder_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='valuation',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=17),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='price',
            field=models.DecimalField(decimal_places=4, max_digits=17, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.DecimalField(decimal_places=4, max_digits=17, null=True),
        ),
    ]
