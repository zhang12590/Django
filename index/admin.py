from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = u'汉源信息平台管理'
admin.site.site_title = u'信息管理'
admin.site.register(Goods)
admin.site.register(ChildrenGoods)