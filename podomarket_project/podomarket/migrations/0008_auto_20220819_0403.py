# Generated by Django 2.2 on 2022-08-19 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podomarket', '0007_auto_20220817_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='item_condition',
            field=models.CharField(choices=[('새제품', '새제품'), ('최상', '최상'), ('상', '상'), ('중', '중'), ('하', '하')], default=None, max_length=10),
        ),
    ]
