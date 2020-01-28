# Generated by Django 2.2.6 on 2019-11-26 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=3)),
                ('price', models.DecimalField(decimal_places=2, max_digits=999999)),
                ('material_type', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='clothes/images/')),
                ('available_stock', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
