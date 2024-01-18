from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', editable=False)
    title = models.CharField('Название', max_length=50, default='')
    anons = models.CharField('Анонс', max_length=250)
    img = models.ImageField('Кртинка')
    ll_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации', auto_now_add=True)



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='Статья')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    text = models.TextField('Текст комментария')
    created_date = models.DateTimeField('Дата создания', auto_now_add=True)

    def str(self):
        return f'{self.user.username} - {self.created_date}'

    def get_absolute_url(self):
        return reverse('detal', args=[str(self.id)])

    def __str__(self):
        return f'{self.user.username} - {self.created_date}'

    def __str__(self):
        return f'{self.user.username} - {self.created_date}'
