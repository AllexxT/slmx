from django.db import models
from versatileimagefield.fields import VersatileImageField, PPOIField
from django.templatetags.static import static


class Social(models.Model):
    socName = models.CharField(
        'Название соц сети', max_length=50, blank=False
    )
    link = models.CharField('Ccылка на социальную сеть', max_length=50)
    socialImage = VersatileImageField(
        verbose_name='Своя иконка социальной сети(Функция не подключена!)', ppoi_field='ppoi',
        blank=True,
        null=True
    )
    ppoi = PPOIField()
    
    INSTAGRAM = 'inst'
    VK = 'vk'
    FACEBOOK = 'fb'
    YOUTUBE = 'yt'
    SOCIALS = (
        (INSTAGRAM, 'Instagram'),
        (FACEBOOK, 'Facebook'),
        (YOUTUBE, 'Youtube'),
        (VK, 'Вконтакте'),
    )

    socIcon = models.CharField(
        'Стандартная иконка', max_length=50, choices=SOCIALS,
        default=None, null=True, blank=True
    )

    def iconUrl(self):
        if not self.socIcon:
            return None
        return static(f'frontend/icons/{self.socIcon}.png')

    def __str__(self):
        return self.link

    class Meta:
        verbose_name_plural = 'Ссылки на соц сети'
        verbose_name = 'Ссылка на соц сеть'


class Phone(models.Model):
    number = models.CharField('Номер телефона', max_length=50)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name_plural = 'Номера телефонов'
        verbose_name = 'Номер телефона'


class Email(models.Model):
    email = models.CharField('Эмайл', max_length=50)
    
    def save(self, *args, **kwargs):
        emails = Email.objects.all()
        if len(emails) >= 1:
            prevEmail = emails[0]
            prevEmail.email = self.email
            super(Email, prevEmail).save()
            return
        super(Email, self).save(*args, **kwargs)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Email'
        verbose_name = 'Email'
