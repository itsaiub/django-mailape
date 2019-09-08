from django.urls import path
from . import views
from . import views

app_name = 'mailinglist'


urlpatterns = [
    path('', views.MailingList.as_view(), name='mailinglist_list'),
    path('new/', views.CreateMailingList.as_view(),
         name='create_mailinglist'),
    path('mailinglist/<uuid:pk>/delete', views.DeleteMailingList.as_view(),
         name='delete_mailinglist'),
    path('mailinglist/<uuid:pk>/manage',
         views.DetailMailingList.as_view(), name='manage_mailinglist'),
]
