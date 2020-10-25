from django.contrib import admin
from frontend.models import (
    Social, Phone, Email
)


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    fields = (
        'socName',
        ('link',
        'socIcon',),
        'socialImage',
    )
    list_display = (
        'socName',
        'link',
        'socIcon',
        'socialImage',
    )
@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    fields = (
        'number',
    )
    list_display = (
        'number',
    )
@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    fields = (
        'email',
    )
    list_display = (
        'email',
    )