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
    categoryName = models.CharField(
        'Название категории', max_length=2,
        choices=CATEGORIES, primary_key=True,
    )
    slugUrl = models.CharField(
        'Адрес страницы', max_length=200, null=True,
        blank=True
    )
    
    def get_absolute_url(self):
        return self.slugUrl

    def readableCategory(self):
        for item in self.CATEGORIES:
            if item[0] == self.categoryName:
                return str(item[1])
    
    def products(self):
        return self.product_set.all()
    
    categoryImage = VersatileImageField(
        verbose_name='Image', ppoi_field='ppoi', blank=True,
        null=True
    )
    ppoi = PPOIField()

    def __str__(self):
        for item in self.CATEGORIES:
            if item[0] == self.categoryName:
                return str(item[1])
        return str(self.categoryName)

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
    price = models.FloatField('Цена', blank=True, null=True)
    title = models.CharField(
        "СЕО  Заголовок", max_length=165, null=True, blank=True,
        default=''
    )
    seoDescription = models.TextField(
        'СЕО описание страницы с товаром(скрытое)', blank=True, null=True
    )
    seoKeywords = models.TextField(
        'СЕО ключевые фразы', blank=True, null=True
    )
    description = RichTextField('Описание на странице', null=True, blank=True)
    position = models.FloatField(
        'Позиция', blank=True, null=True, default=0
    )
    discount = models.BooleanField('Скидка', blank=True, default=False)
    sertificate = models.BooleanField('Сертификат', blank=True, default=False)
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.CASCADE
    )
    
    def seoInfo(self):
        if len(self.seoDescription) == 0 and self.title == None:
            return 'Отсутствует'
        elif len(self.seoDescription) != 0 and self.title != None:
            return 'Настроено'
        else:
            return 'Не полное'
        return 'Ошибка'
    seoInfo.short_description = 'SEO товара'

    # VersatileImageField
    productImage = VersatileImageField(
        verbose_name='Photo', ppoi_field='ppoi', blank=True,
    )
    ppoi = PPOIField()

    # UUSLUG
    slug = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ['-position']
############################### Product end #


