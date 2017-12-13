from django.db import models

# Create your models here.

class Users(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    uid=models.AutoField(primary_key=True)
class WebPage(models.Model):
    webname=models.CharField(max_length=32)
    weburl=models.CharField
    webimg=models.CharField
    webdescribe=models.CharField(max_length=32)
    webtab=models.CharField(max_length=32)
    webclass_choice=((1,'设计'),(2,'代码'),(3,'模型'),(4,'其他'))
    webclass_id=models.IntegerField(choices=webclass_choice)
    wid=models.ForeignKey('Users',to_field="uid")
class WebcategorySub(models.Model):
    webcategory1_choice = ((100, '设计导航'), (101, '设计素材'), (102, '设计理论'), (103, '设计收藏'))
    webcategory2_choice = ((200, 'python'), (201, 'javascript'), (202, 'html5'), (203, 'css3'), (204, 'css3'), (205, 'git'), (206, 'vue'), (207, 'node'), (208, 'angular'), (209, 'react'), (210, 'linux'), (211, 'php'), (212, 'c'), (213, 'mysql'))
    webcategory3_choice = ((300,'3dMax'),(301,'AE'))
    webcategory4_choice = ((400,'游戏'),(401,'其他'))
    webcategory_choice = webcategory1_choice+webcategory2_choice+webcategory3_choice+webcategory4_choice
    webcategory_id = models.IntegerField(choices=webcategory_choice)
    wsid=models.ForeignKey('Users',to_field='uid')


