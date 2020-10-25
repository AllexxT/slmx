from frontend.models import (
    Social, Phone, Email,
)

def frontend_processor(request):
    social = Social.objects.all()[:3]
    phones = Phone.objects.all()[:2]
    email = Email.objects.all().first()
    return {
        'frontend': {
            'social': social,
            'phones': phones,
            'email': email,
        }
    }