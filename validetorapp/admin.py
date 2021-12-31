from django.contrib import admin
from .models import email_details ,user,phone_details
# register the models here.
admin.site.register(email_details)
admin.site.register(user)
admin.site.register(phone_details)