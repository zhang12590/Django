from django.db import models

# Create your models here.
class Goods(models.Model):
    name = models.CharField(max_length=50, null=False,verbose_name=u'名称')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = u'父栏目'
        verbose_name_plural = verbose_name

class ChildrenGoods(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name=u'名称')
    foreiginkey = models.ForeignKey(Goods, on_delete=True, verbose_name=u'所属栏目')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = u'子栏目'
        verbose_name_plural = verbose_name