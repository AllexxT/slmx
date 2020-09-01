from django.contrib import admin

from catalog.models import (
    Category, Page, Product, Benefits, Specific
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


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    class BenefitsInline(admin.TabularInline):
        model = Benefits
        extra = 0

    class SpecificInline(admin.TabularInline):
        model = Specific
        extra = 0
    inlines = [BenefitsInline, SpecificInline]

    fields = (
        'name',
        'category',
        'position',
        'seoDescription',
        'seoKeywords',
        'description',
        'productImage',
    )
    list_display = (
        'name',
        'description',
    )
