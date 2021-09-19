
from random import randint
from urllib.parse import urlparse
from django.core.cache import cache
from django.shortcuts import render,redirect
from django.urls import path
from django.utils.baseconv import base56
from django.conf import settings
import os.path
from django.core.management import execute_from_command_line


settings.configure(
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)),
    ROOT_URLCONF=__name__,
    DEBUG=True,
    SECRET_KEY='secret'
)
ALLOWED_SCHEMES = {'http', 'https', 'ftp'}
MIN_KEY, MAX_KEY = 80106440, 550731775

def redirect_key(request, key):
    return redirect(to=cache.get(key, '/'))

def index(request):
    ctx = {}
    if request.POST:
        url = request.POST.get('url')
        if urlparse(url).scheme in ALLOWED_SCHEMES:
            key = base56.encode(randint(MIN_KEY,MAX_KEY))
            cache.add(key, url)
            ctx['key'] = key
        else:
            ctx['messege'] = f'Invalid URL {url}. Allomed schemes: ' + ','.join(ALLOWED_SCHEMES)
    return render(request, 'zan.html', ctx)
urlpatterns = [
    path('', index, name='index'),
    path('<key>', redirect_key, name = 'redirect-key'),

]
if __name__ == '__main__':
    execute_from_command_line()
