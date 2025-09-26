
from django.urls import path, include

from django.contrib import admin

urlpatterns = [
    path('todo/', include('todo.urls')),
    path('', include('todo.urls')),
    path('admin/', admin.site.urls),
]
