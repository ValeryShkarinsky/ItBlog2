# Generated by Django 4.2.7 on 2024-01-18 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainblog', '0005_alter_article_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='Кртинка'),
        ),
    ]