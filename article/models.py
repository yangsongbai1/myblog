from django.db import models
from django.utils.timezone import now, localtime


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=254)
    # author = models.ForeignKey('User', on_delete=models.SET_NULL)
    create_time = models.DateTimeField(auto_now_add=now)
    modify_time = models.DateTimeField(auto_now=now)
    tags = models.ManyToManyField('Tag')
    content = models.TextField()
    removed = models.BooleanField()
    # comment = models.ForeignKey('Comment', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'article'
        verbose_name = '博客文章'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tags'
        verbose_name = '标签'
        verbose_name_plural = verbose_name


# 评论
# class Comment(models.Model):
#     id = models.AutoField(primary_key=True)
#     comment = models.TextField()
#
#     class Meta:
#         db_table = 'comments'
#         verbose_name = '评论'
#         verbose_name_plural = verbose_name
