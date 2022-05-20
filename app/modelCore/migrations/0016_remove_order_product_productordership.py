# Generated by Django 4.0.4 on 2022-05-19 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelCore', '0015_order_product_delete_productordership'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.CreateModel(
            name='ProductOrderShip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelCore.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='modelCore.product')),
            ],
        ),
    ]