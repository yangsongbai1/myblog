from django.db import models


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=254)
    date = models.TimeField()
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'article'
        verbose_name = '博客文章'
        verbose_name_plural = verbose_name
