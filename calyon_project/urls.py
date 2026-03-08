# calyon_project/urls.py
from django.contrib import admin
from django.urls import path, include # <-- include'u eklemeyi unutmayın!

urlpatterns = [
    path('admin/', admin.site.urls),
    # /api/ ile başlayan her şeyi calyon_app içindeki urls.py'ye gönder
    path('api/', include('calyon_app.urls')), 
]