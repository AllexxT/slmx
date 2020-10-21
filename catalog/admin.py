from django.contrib import admin

from catalog.models import (
    Category, Product, Benefits, Specific
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    fields = (
        'categoryName',
        'slugUrl',
        'categoryImage',
    )

    list_display = (
        'categoryName',
        'slugUrl',
        'categoryImage'
    )
    # radio_fields = {"_category": admin.HORIZONTAL}


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
        ('price',
         'nds',
        'position'),
        'title',
        'seoDescription',
        'seoKeywords',
        'description',
        'productImage',
        ('discount',
        'sertificate',)
    )
    list_display = (        
        'name',
        'price',
        'discount',
        'sertificate',
        'category',
        'position',
        'seoInfo'
    )
    list_filter = ('category',)
    search_fields = ['name']
    save_on_top = True
