from django.contrib import admin
from django.urls import path, include

from django.conf import settings

# Added to change the title, header which is first Django Administration
admin.site.site_header = "Pie Bank of India Admin Panel"
admin.site.site_title = "PBI Admin Portal"
admin.site.index_title = "Welcome to Pie Bank Of India"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pie_bank_app.urls')),
]
