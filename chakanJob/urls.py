
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hr/', include('hr.urls')),
    path('', include('job.urls')),
]
