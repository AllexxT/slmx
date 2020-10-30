from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from django.core.exceptions import ValidationError
from pages.models import (
    Page, InPageImages, InPageFiles, InPageImages,
    OurWorks,
    Contacts, ContactsText,
)
from silmix.settings import DEBUG
# import pprint
# pp = pprint.PrettyPrinter(width=80, compact=True)

if DEBUG == False:
    class PageFormSet(BaseInlineFormSet):

        def clean(self):
            super(PageFormSet, self).clean()
            print(self.__dict__)
            for form in self.forms:
                if not hasattr(form, 'cleaned_data'):
                    continue

                data = form.cleaned_data
                curr_instance = form.instance

                print(form.instance.__dict__)
                print(data)
                if (data.get('DELETE')):
                    raise ValidationError('Удаление запрещено')


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):

    class ImagesInline(admin.TabularInline):
        model = InPageImages
        extra = 0
        if DEBUG == False:
            formset = PageFormSet
            readonly_fields = ('imageName',)
        exclude = ('ourWorks',)

    class FilesInline(admin.TabularInline):
        model = InPageFiles
        extra = 0
        if DEBUG == False:
            formset = PageFormSet
            readonly_fields = ('fileName',)
    inlines = [ImagesInline, FilesInline]

    fields = (
        'page',
        'title',
        'description',
        'keywords',
        'readableTitle',
        'body',
    )
    list_display = (
        'readableTitle',
        'page',
        'title',
        'keywordsLength',
        'descriptionLength',
    )
    save_on_top = True
    if DEBUG == False:
        readonly_fields = ('page',)


@admin.register(OurWorks)
class OurWorksAdmin(admin.ModelAdmin):

    class ImagesInline(admin.TabularInline):
        model = InPageImages
        extra = 0
        exclude = ('page',)

    inlines = [ImagesInline, ]
    list_filter = ('category',)
    save_on_top = True

    fields = (
        'category',
        'title',
        'address',
        'description',
    )
    list_display = (
        'category',
        'title',
        'address',
    )


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    
    class TextInline(admin.TabularInline):
        model = ContactsText
        extra = 0
    inlines = [ TextInline, ]
    save_on_top = True
    
    fields = (
        'position',
        'h2',
        # 'allTexts',
    )
    
    list_display = (
        'h2',
        'position',
        'allTexts',
    )
