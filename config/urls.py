from django.contrib import admin
from django.urls import path, include
from mailinglist import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls', namespace='user')),
    path('mailinglist/', include('mailinglist.urls', namespace='mailinglist')),
    path('', views.MailingList.as_view(), name='home')
]
