from django.db import models
from DjangoUeditor.models import UEditorField
from index.models import ChildrenGoods
# Create your models here.
class Detail(models.Model):
    foreiginkey = models.ForeignKey(ChildrenGoods, on_delete=True, verbose_name=u'类别')
    title = models.CharField(max_length=50,verbose_name=u'标题')
    content = UEditorField(u'详细内容', height=900, width=1600, toolbars='full', blank=True, imagePath="image/",)
    class Meta:
        verbose_name = u"文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title