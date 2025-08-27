from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField('투자상품', max_length = 100)
    description = models.TextField('상품설명')
    create_at=models.TimeField('생성일',auto_now=True)