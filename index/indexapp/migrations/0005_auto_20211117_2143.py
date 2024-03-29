# Generated by Django 3.2.8 on 2021-11-17 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0004_foods'),
    ]

    operations = [
        migrations.AddField(
            model_name='foods',
            name='category',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='内容'),
        ),
        migrations.AddField(
            model_name='foods',
            name='cutomer',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='得意先'),
        ),
        migrations.AddField(
            model_name='foods',
            name='register',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='カクテル登録'),
        ),
        migrations.AddField(
            model_name='foods',
            name='supplier',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='仕入先'),
        ),
        migrations.AddField(
            model_name='foods',
            name='update',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='リスト更新'),
        ),
        migrations.AddField(
            model_name='foods',
            name='writer',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='依頼書作成'),
        ),
        migrations.AddField(
            model_name='registration',
            name='category',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='内容'),
        ),
        migrations.AddField(
            model_name='registration',
            name='register',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='カクテル登録'),
        ),
        migrations.AddField(
            model_name='registration',
            name='supplier',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='仕入先'),
        ),
        migrations.AddField(
            model_name='registration',
            name='update',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='リスト更新'),
        ),
        migrations.AddField(
            model_name='registration',
            name='writer',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='依頼書作成'),
        ),
    ]
