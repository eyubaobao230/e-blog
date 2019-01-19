from django.db import models


# 创建文章模型
class Article(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=300)
    content = models.TextField()
    # icon = models.ImageField(upload_to='article', null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta():
        db_table = 'article'


# 创建登录模型
class SuperUser(models.Model):
    username = models.CharField(max_length=5, unique=True)
    password = models.CharField(max_length=5)
    create_time = models.DateTimeField(auto_now_add=True)
    recreate_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'superuser'




