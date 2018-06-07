from django.db import models

# Create your models here.

# 包名和模块名: 简短全小写的名字
# 类名: 首字母大写
# 常量: 下划线分隔的全大写字母
# 法名和实例变量: 下划线分隔小写单词


class User(models.Model):
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    name = models.CharField(max_length=20, null=True)
    telephone = models.IntegerField(null=True)


class Group(models.Model):
    group_name = models.CharField(max_length=30)


class Project(models.Model):
    STATUS = (
        ('1', '待进行'),
        ('2', '进行中'),
        ('3', '暂停'),
        ('4', '完成'),
        ('5', '关闭'),
        ('6', '延期')
    )
    project_name = models.CharField(max_length=30)
    create_time = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    status = models.CharField(max_length=2, choices=STATUS, default='1')
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)


class Task(models.Model):
    STATUS = (
        ('1', '待进行'),
        ('2', '进行中'),
        ('3', '暂停'),
        ('4', '完成'),
        ('5', '关闭'),
    )
    task_name = models.CharField(max_length=30)
    create_time = models.DateField(auto_now_add=True)
    planned_working_hours = models.FloatField()
    actual_working_hours = models.FloatField()
    task_content = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)


class Grouping(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)