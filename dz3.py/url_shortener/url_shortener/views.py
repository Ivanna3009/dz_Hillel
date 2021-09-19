
from random import randint
from urllib.parse import urlparse
from django.core.cache import cache
from django.shortcuts import render,redirect
from django.urls import path
from django.utils.baseconv import base56
import os.path

ALLOWED_SCHEMES = {'http', 'https', 'ftp'}
MIN_KEY = 80106440
MAX_KEY = 550731775

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
    return render(request, 'index.html', ctx)
