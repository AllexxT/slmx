from django.db import models
from ckeditor.fields import RichTextField
from versatileimagefield.fields import VersatileImageField, PPOIField
from catalog.models import Category


class InPageImages(models.Model):
    page = models.ForeignKey(
        "Page", verbose_name='Страница', on_delete=models.CASCADE,
        null=True
    )
    ourWorks = models.ForeignKey(
        "OurWorks", verbose_name='Наши работы', on_delete=models.CASCADE,
        null=True
    )
    imageName = models.CharField('Название', max_length=50, null=True, blank=True)
    pageImage = VersatileImageField(
        verbose_name='Image', ppoi_field='ppoi', blank=False,
        null=True
    )
    ppoi = PPOIField()

    def __str__(self):
        return self.imageName
    class Meta:
        verbose_name_plural = 'Изображения на странице'
        verbose_name = 'Изображение'


class InPageFiles(models.Model):
    page = models.ForeignKey(
        "Page", verbose_name='Страница', on_delete=models.CASCADE,
        null=True
    )
    fileName = models.CharField('Название', max_length=50)
    file = models.FileField('Файл', blank=True, null=True)

    def __str__(self):
        return self.fileName
    class Meta:
        verbose_name_plural = 'Файлы страницы'
        verbose_name = 'Файл'


class Page(models.Model):
    page = models.CharField("Страница", max_length=30, primary_key=True)
    title = models.CharField(
        "СЕО  Заголовок", max_length=165, null=True, blank=True)
    readableTitle = models.CharField(
        "Заголовок на странице", max_length=165, null=True, blank=True)
    description = models.TextField(
        "СЕО Описание(скрытое)", blank=True, null=True)
    keywords = models.TextField(
        "СЕО Ключевые слова", blank=True, null=True)
    body = RichTextField(
        "Текст на странице", blank=True, null=True)

    def keywordsLength(self):
        if self.keywords == None or len(self.keywords.split(',')) <= 1:
            return "Нет ключевых фраз"
        return f"Количество ключевых фраз - «{len(self.keywords.split(','))}»"
    keywordsLength.short_description = 'Ключевые фразы SEO'

    def descriptionLength(self):
        if self.description == None or len(self.description.split(' ')) <= 1:
            return "SEO описание отсутствует"
        return f"Количество слов в SEO описании - «{len(self.description.split(' '))}»"
    descriptionLength.short_description = 'SEO описание'

    def __str__(self):
        return str(self.page)

    class Meta:
        verbose_name_plural = 'Страницы и СЕО'
        verbose_name = 'Страницу СЕО'


class OurWorks(models.Model):
    title = models.CharField('Заголовок', max_length=150, blank=True, null=True)
    address = models.CharField('Адрес', max_length=100, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    
    CHOICES = (
        ('ALL', 'Без категории'),
        *Category.CATEGORIES,
    )
    
    category = models.CharField('Категория', max_length=10, null=True,
                                choices=CHOICES, default=CHOICES[0][0])

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = 'Галерея наших работ'
        verbose_name = 'Фото наших работ'


class Contacts(models.Model):
    h2 = models.CharField(
        'Заголовок контактной информации', max_length=150,
        blank=True, null=True
    )
    position = models.IntegerField(
        "Позиция на странице", null=True, blank=True
    )

    def allTexts(self):
        return f'{len(self.contactstext_set.all())}'
    allTexts.short_description = "Количество текстовых блоков"

    def __str__(self):
        return self.h2
    
    class Meta:
        ordering = ['-position']
        verbose_name_plural = 'Контактная информация'
        verbose_name = 'Контактную информацию'
    

class ContactsText(models.Model):
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    text = RichTextField('Контактная информация', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Текст контактной информации'
        verbose_name = 'Текст контактной информации'
