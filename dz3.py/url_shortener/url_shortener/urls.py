
from django.contrib import admin
from django.urls import path

import url_shortener.views as v
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', v.index, name='index'),
    path('<key>', v.redirect_key, name = 'redirect-key'),
]
