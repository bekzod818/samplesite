from django.contrib import admin
from django.urls import path
from bboard.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bboard/', index)
]
