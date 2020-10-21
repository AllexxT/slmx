from pages.models import Page
import json

print('Importing pagesMeta.json')
pages = json.load(open('pagesMeta.json'))

print('Creating pages')
for item in pages:
    Page(readableTitle=item[0], page=item[1]).save()

print('Creating pages is finiched')