from django.db import models


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=254)
    # author = models.ForeignKey('User', on_delete=models.SET_NULL)
    date = models.TimeField()
    tags = models.ManyToManyField('Tag')
    content = models.TextField()
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'article'
        verbose_name = '博客文章'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Comment(models.Model):
    comment = models.TextField()