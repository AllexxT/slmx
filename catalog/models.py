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
        choices=CATEGORIES, primary_key=True
    )
    
    categoryImage = VersatileImageField(
        verbose_name='Photo', ppoi_field='ppoi', blank=True
    )
    ppoi = PPOIField()

    def __str__(self):
        for item in self.CATEGORIES:
            if item[0] == self._category:
                return str(item[1])
        return str(self._category)

    class Meta:
        verbose_name_plural = 'Категории товаров'
        verbose_name = 'Категория товаров'

# Product ###############################
class Benefits (models.Model):
    benefit = models.CharField('Преимущество', max_length=150)
    product = models.ForeignKey(
        'Product', verbose_name="Продукт", on_delete=models.CASCADE,
        null=True
    )
    def __str__(self):
        return str(self.benefit)
    class Meta:
        verbose_name_plural = 'Преимущества'
        verbose_name = ' '


class Specific (models.Model):
    specific = models.CharField('Спецификация', max_length=150)
    value = models.CharField('Значение', max_length=150, blank=True)
    product = models.ForeignKey(
        'Product', verbose_name="Продукт", on_delete=models.CASCADE,
        null=True
    )
    def __str__(self):
        return f'{self.specific} - {self.value}'

    class Meta:
        verbose_name_plural = 'Технические данные'
        verbose_name = 'Технические данные'


class Product(models.Model):
    name = models.CharField('Название', max_length=150)
    seoDescription = models.TextField(
        'СЕО описание страницы с товаром(скрытое)', blank=True, null=True
    )
    seoKeywords = models.TextField(
        'СЕО описание страницы с товаром(скрытое)', blank=True, null=True
    )
    description = RichTextField('Описание на странице', null=True, blank=True)
    position = models.FloatField(
        'Позиция товара в списке товаров', blank=True, null=True, default=0
    )
    productImage = VersatileImageField(
        verbose_name='Photo', ppoi_field='ppoi', blank=True
    )
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.CASCADE
    )

    # UUSLUG
    slug = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ['-position']
############################### Product end #


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
