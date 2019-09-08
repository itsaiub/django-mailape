from django.urls import path
from . import views
from . import views

app_name = 'mailinglist'


urlpatterns = [
    path('', views.MailingList.as_view(), name='mailinglist_list'),
    path('new/', views.CreateMailingList.as_view(),
         name='create_mailinglist'),
]
