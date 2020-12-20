from django.db import models

# Create your models here.

class Work(models.Model):
    title = models.CharField('タイトル', max_length=100)
    image = models.ImageField(upload_to='images', verbose_name='イメージ画像')
    thumbnail = models.ImageField(upload_to='images', verbose_name='サムネイル', null=True, blank=True)
    skill = models.CharField('スキル', max_length=100)
    url = models.CharField('URL', max_length=100, null=True, blank=True)
    created = models.DateField('作成日時')
    description = models.TextField('説明')

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField('スキル名', max_length=100)
    percentage = models.IntegerField('パーセンテージ')

    def __str__(self):
        return self.name