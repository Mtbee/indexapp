from django.db import models

# Create your models here.

class Progress(models.Model):
    number = models.IntegerField("No.", unique=True)
    code = models.IntegerField("コード", blank=True, null=True)
    name = models.CharField("品名", max_length=30, blank=True, null=True)
    quantity = models.IntegerField("数量", blank=True, null=True)
    unit = models.CharField("単位", max_length=30, blank=True, null=True)
    order = models.DateField("発注日", blank=True, null=True)
    prefer = models.DateField("希望納期", blank=True, null=True)
    fixed = models.DateField("確定納期", blank=True, null=True)
    description = models.TextField("備考", blank=True, null=True)

    def __str__(self):
        return self.name


class Registration(models.Model):
    number = models.IntegerField("No.", unique=True)
    code = models.IntegerField("コード", blank=True, null=True)
    name = models.CharField("品名", max_length=30, blank=True, null=True)
    category = models.CharField("内容", max_length=30, blank=True, null=True)
    supplier = models.CharField("仕入先", max_length=30, blank=True, null=True)    
    description = models.TextField("備考", blank=True, null=True)
    writer = models.CharField("依頼書作成", max_length=30, blank=True, null=True)
    register = models.CharField("カクテル登録", max_length=30, blank=True, null=True)
    update = models.CharField("リスト更新", max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name


class Foods(models.Model):
    number = models.IntegerField("No.", unique=True)
    code = models.IntegerField("コード", blank=True, null=True)
    name = models.CharField("品名", max_length=30, blank=True, null=True)
    category = models.CharField("内容", max_length=30, blank=True, null=True)
    supplier = models.CharField("仕入先", max_length=30, blank=True, null=True)
    cutomer = models.CharField("得意先", max_length=30, blank=True, null=True)     
    description = models.TextField("備考", blank=True, null=True)
    writer = models.CharField("依頼書作成", max_length=30, blank=True, null=True)
    register = models.CharField("カクテル登録", max_length=30, blank=True, null=True)
    update = models.CharField("リスト更新", max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name


class Estimate(models.Model):
    number = models.IntegerField("No.", unique=True)
    client = models.CharField("見積先", max_length=30, blank=True, null=True)
    name = models.CharField("品名", max_length=30, blank=True, null=True)
    form = models.CharField("形態", max_length=30, blank=True, null=True)
    deadline = models.CharField("企画期限", max_length=30, blank=True, null=True)
    requester = models.CharField("依頼部門", max_length=30, blank=True, null=True)
    description = models.TextField("備考", blank=True, null=True)     
    responder = models.TextField("担当者", blank=True, null=True)

    def __str__(self):
        return self.name
