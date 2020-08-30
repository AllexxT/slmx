from django.contrib import admin

from catalog.models import (
    Category, Page,
)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    fields = (
        'page',
        'readableTitle',
        'title',
        'description',
        'keywords',
        'body',
    )
    list_display = (
        'page',
        'readableTitle',
        'title',
        'description',
        'keywordsLength',
        'body',
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = (
        '_category',
        'categoryImage'
    )
    list_display = (
        '_category',
        'categoryImage'
    )
