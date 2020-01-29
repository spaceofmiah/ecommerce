# Generated by Django 3.0 on 2020-01-28 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clothing', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('available_in_stock', models.IntegerField(default=1)),
                ('review', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='clothing.Cloth')),
            ],
            options={
                'verbose_name': 'Cart Item',
                'verbose_name_plural': 'Cart Item',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('ticket', models.CharField(editable=False, max_length=100)),
                ('pending', models.BooleanField(default=True)),
                ('items', models.ManyToManyField(related_name='belongs_to', to='cart.CartItem')),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Cart',
            },
        ),
    ]
