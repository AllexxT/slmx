from django.db import models
from ckeditor.fields import RichTextField
from versatileimagefield.fields import VersatileImageField, PPOIField
from uuslug import uuslug
from datetime import date


class Category(models.Model):
    UTEPLENIE = 'UT'
    POL = 'PO'
    KLADKA = 'KL'
    OBLICOVKA = 'OB'
    SHTUKATURKA = 'SH'

    CATEGORIES = (
        (UTEPLENIE, 'Смеси для утепления'),
        (POL, 'Смеси для пола'),
        (KLADKA, 'Кладочные смеси'),
        (OBLICOVKA, 'Смеси для облицовки'),
        (SHTUKATURKA, 'Штукатурные смеси'),
    )
    _category = models.CharField(
        'Категория', max_length=2,
        choices=CATEGORIES
    )
    
    categoryImage = VersatileImageField(
        verbose_name='Photo', ppoi_field='ppoi', blank=True
    )
    ppoi = PPOIField()

    def __str__(self):
        return str(self._category)

    class Meta:
        verbose_name_plural = 'Категории товаров'
        verbose_name = 'Категория товаров'


class Page(models.Model):
    page = models.CharField("Страница", max_length=30, primary_key=True)
    title = models.CharField(
        "СЕО  Заголовок", max_length=165, null=True, blank=True)
    readableTitle = models.CharField(
        "Читаемый заголовок", max_length=165, null=True, blank=True)
    description = models.TextField(
        "СЕО Описание(скрытое)", blank=True, null=True)
    keywords = models.TextField(
        "СЕО Ключевые слова", blank=True, null=True)
    body = RichTextField(
        "Текст на странице", blank=True, null=True)

    def keywordsLength(self):
        if len(self.keywords.split(',')) <= 1:
            return "Нет ключевых фраз"
        return f"Количество ключевых фраз - «{len(self.keywords.split(','))}»"
    def __str__(self):
        return str(self.page)

    class Meta:
        verbose_name_plural = 'Страницы СЕО'
        verbose_name = 'Страницу СЕО'