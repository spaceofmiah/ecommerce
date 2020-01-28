# Generated by Django 3.0 on 2020-01-28 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20191206_2025'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Cart', 'verbose_name_plural': 'Cart'},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name': 'Cart Item', 'verbose_name_plural': 'Cart Item'},
        ),
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(related_name='belongs_to', to='cart.CartItem'),
        ),
    ]
