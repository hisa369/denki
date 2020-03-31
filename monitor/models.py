from django.db import models
from django.urls import reverse
from datetime import datetime as dt


class Location(models.Model):
    """場所モデル"""
    class Meta:
        db_table = 'location'

    name = models.CharField(verbose_name='対象箇所', max_length=255)
    memo = models.CharField(verbose_name='メモ', max_length=255, default='', blank=True)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    def __str__(self):
        return self.name + "(" + self.memo + ")"

    @staticmethod
    def get_absolute_url(self):
        return reverse('monitor:index')

    class Meta:
        verbose_name = '場所'
        verbose_name_plural = '場所'



class WeatherData(models.Model):
    """気象データモデル"""
    class Meta:
        db_table = 'weather_data'
        unique_together = (('location', 'nengetu'),)

    location = models.ForeignKey(Location, verbose_name='対象箇所', on_delete=models.PROTECT)
    nengetu = models.CharField('年月', max_length=6, default=202001)
    dentou = models.IntegerField('電灯使用量', default=0)
    kuchou = models.IntegerField('空調使用量', default=0)
    goukei = models.IntegerField('合計', default=0)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    def __str__(self):
        return self.location.name + "(" + self.nengetu + ")"

    class Meta:
        verbose_name = 'データ'
        verbose_name_plural = 'データ'
