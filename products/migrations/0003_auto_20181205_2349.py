# Generated by Django 2.1.3 on 2018-12-05 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20181202_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='total_votes',
            field=models.IntegerField(default=1),
        ),
    ]
