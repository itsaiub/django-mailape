from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls', namespace='user')),
    path('mailinglist/', include('mailinglist.urls', namespace='mailinglist')),
]
