from django.db import models

from .config import *


# Create your models here.
class Target(models.Model):
    url = models.URLField(verbose_name='网址')
    name = models.CharField(max_length=50, verbose_name="网站名")
    status = models.PositiveIntegerField(choices=STATUS_ITEM, default=STATUS_NORMAL,
                                         verbose_name='状态')
    describe = models.CharField(max_length=500, verbose_name="简介")
    category = models.CharField(max_length=50, verbose_name="分类")

    class Meta:
        verbose_name = verbose_plural_name = '网站'
