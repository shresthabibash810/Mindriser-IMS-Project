# Generated by Django 5.0.7 on 2024-08-05 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='department',
            field=models.ManyToManyField(null=True, to='base.department'),
        ),
    ]
