# Generated by Django 3.0.8 on 2020-08-15 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0024_auto_20200815_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]
