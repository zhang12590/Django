from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.
class Goods(models.Model):
    name = models.CharField(max_length=50, null=False)

class ChildrenGoods(models.Model):
    name = models.CharField(max_length=50, null=False)
    foreiginkey = models.ForeignKey(Goods, on_delete=True)