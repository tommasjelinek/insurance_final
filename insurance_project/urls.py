from django.contrib import admin
from django.urls import path, include

from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('insurance_app.urls')),

    #path(r'^$', include('insurance_app.urls')),


]
