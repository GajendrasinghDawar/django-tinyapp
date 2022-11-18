from django.urls import path
from django.template.response import TemplateResponse

DEBUG = True
SECRET_KEY = '4l0ngs3cr3tstr1ngw3lln0ts0l0ngw41tn0w1tsl0ng3n0ugh'
ROOT_URLCONF = __name__
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': ['templates', ]
},
]


def tinyapp(request):
    response = TemplateResponse(request, 'index.html', {
                                'author': 'Gajendrasingh Dawar'})
    return response


urlpatterns = [
    path('', tinyapp)
]
