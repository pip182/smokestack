# Generated by Django 2.2.8 on 2019-12-17 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='quantity',
            new_name='current_quantity',
        ),
    ]
