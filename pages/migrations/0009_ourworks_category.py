# Generated by Django 3.1 on 2020-09-07 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20200907_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourworks',
            name='category',
            field=models.CharField(choices=[('ALL', 'Все категории'), ('UT', 'Смеси для утепления'), ('PO', 'Смеси для пола'), ('KL', 'Кладочные смеси'), ('OB', 'Смеси для облицовки'), ('SH', 'Штукатурные смеси')], default='ALL', max_length=10, null=True, verbose_name='Категория'),
        ),
    ]
