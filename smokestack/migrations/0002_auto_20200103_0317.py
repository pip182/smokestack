# Generated by Django 3.0.1 on 2020-01-03 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smokestack', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='position',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='departmentwork',
            name='position',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='position',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='projectphase',
            name='position',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
        ),
    ]
