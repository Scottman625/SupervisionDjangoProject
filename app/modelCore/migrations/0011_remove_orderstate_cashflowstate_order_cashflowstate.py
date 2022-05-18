# Generated by Django 4.0.4 on 2022-05-13 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelCore', '0010_orderstate_alter_order_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderstate',
            name='cashflowState',
        ),
        migrations.AddField(
            model_name='order',
            name='cashflowState',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]