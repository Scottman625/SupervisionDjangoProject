# Generated by Django 4.0.4 on 2022-05-19 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelCore', '0014_remove_order_product_productordership'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(to='modelCore.product'),
        ),
        migrations.DeleteModel(
            name='ProductOrderShip',
        ),
    ]