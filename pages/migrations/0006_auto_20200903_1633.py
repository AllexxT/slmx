# Generated by Django 3.1 on 2020-09-03 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20200903_1435'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inpageimages',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения на странице'},
        ),
        migrations.CreateModel(
            name='InPageFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileName', models.CharField(max_length=50, verbose_name='Название')),
                ('file', models.FileField(blank=True, null=True, upload_to='', verbose_name='Файл')),
                ('page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.page', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы страницы',
            },
        ),
    ]
