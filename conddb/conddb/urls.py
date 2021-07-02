from django.urls import include, path
from django.contrib import admin


api_urls = [
    path('cdb/', include('cdb.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
]
