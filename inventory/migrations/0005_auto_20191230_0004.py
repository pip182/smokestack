# Generated by Django 3.0.1 on 2019-12-30 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20191229_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='notes',
            field=models.TextField(blank=True, default=''),
        ),
    ]