# Generated by Django 2.1.3 on 2018-12-05 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20181205_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='total_votes',
            field=models.IntegerField(default=2),
        ),
    ]
