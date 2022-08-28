from django.contrib import admin
from django.urls import path, include
from tgQA.views import *
from glpage.views import catAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('glpage.urls')),
]
