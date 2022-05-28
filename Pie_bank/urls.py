from django.contrib import admin
from django.urls import path, include

# Added for hosting
from django.views.static import serve
from django.conf.urls import url

from django.conf import settings

# Added to change the title, header which is first Django Administration
admin.site.site_header = "Pie Bank of India Admin Panel"
admin.site.site_title = "PBI Admin Portal"
admin.site.index_title = "Welcome to Pie Bank Of India"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pie_bank_app.urls')),

    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
