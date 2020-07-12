from django.db import models


class Article(models.Model):
    articleTitle = models.CharField('название статьи', max_length=200)
    articleText = models.TextField('текст статьи')
    pubDate = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.articleTitle

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    authorName = models.CharField('имя автора', max_length=50)
    commentText = models.CharField('текст комментария', max_length=200)

    def __str__(self):
        return self.authorName

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
