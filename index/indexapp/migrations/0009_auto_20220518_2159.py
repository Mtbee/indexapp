# Generated by Django 3.2.8 on 2022-05-18 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0008_auto_20220413_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roulette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='なまえ')),
            ],
        ),
        migrations.AlterField(
            model_name='foods',
            name='code',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='コード'),
        ),
        migrations.AlterField(
            model_name='foods',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='品名'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='code',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='コード'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='品名'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='code',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='コード'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='品名'),
        ),
    ]