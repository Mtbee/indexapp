from django.db import models

# Create your models here.

class Progress(models.Model):
    number = models.IntegerField("No.")
    code = models.IntegerField("コード")
    name = models.CharField("品名", max_length=30, blank=True)
    quantity = models.IntegerField("数量", blank=True)
    unit = models.CharField("単位", max_length=30, blank=True)
    order = models.DateField("発注日", blank=True)
    prefer = models.DateField("希望納期", blank=True)
    fixed = models.DateField("確定納期", blank=True)
    description = models.TextField("備考", blank=True)

    def __str__(self):
        return self.name
