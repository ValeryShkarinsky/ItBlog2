from django.db import models

class Article(models.Model):
    title = models.CharField('Название', max_length=50, default='')
    anons = models.CharField('Анонс', max_length=250)
    img = models.ImageField('Кртинка')
    ll_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title