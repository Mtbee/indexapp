# Generated by Django 3.2.8 on 2022-04-13 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0007_auto_20220413_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiverequest',
            name='responder',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='担当者'),
        ),
        migrations.AlterField(
            model_name='sendrequest',
            name='responder',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='担当者'),
        ),
    ]
