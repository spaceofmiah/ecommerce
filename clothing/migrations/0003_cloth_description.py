# Generated by Django 2.2.6 on 2019-11-08 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0002_auto_20191028_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloth',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]