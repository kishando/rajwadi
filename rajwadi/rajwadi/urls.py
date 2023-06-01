from django.contrib import admin
from django.urls import include, path
from app1 import views

urlpatterns = [
    path('', include('app1.urls')),
    
    path('admin/', admin.site.urls),
]