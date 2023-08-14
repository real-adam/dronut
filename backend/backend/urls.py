"""
backend URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('silk/', include('silk.urls', namespace='silk')),

    path('donuts', include('donuts.urls')),

    path('orders', include('orders.urls')),
]
