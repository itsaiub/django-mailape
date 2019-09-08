from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.MailingList)
admin.site.register(models.Message)
admin.site.register(models.Subscriber)
