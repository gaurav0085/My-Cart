# Generated by Django 2.1 on 2020-07-29 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200729_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.TextField(default='GS', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.TextField(default='GS', max_length=50),
        ),
    ]
