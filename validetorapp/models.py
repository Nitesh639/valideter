from django.db import models

# email_details model for the email data
class email_details(models.Model):
    email_address = models.EmailField(max_length=100)
    domain = models.CharField(max_length=100)
    valid_syntax = models.BooleanField()
    disposable = models.BooleanField()
    webmail = models.BooleanField()
    deliverable = models.BooleanField()
    gibberish = models.BooleanField()
    spam = models.BooleanField()
# phone_details model for the phone data
class phone_details(models.Model):
    status = models.CharField(max_length=15,null=True)
    phone = models.CharField(max_length=15,null=True)
    phone_valid = models.BooleanField(default=False)
    phone_type =  models.CharField(max_length=15,null=True)
    phone_region = models.CharField(max_length=100,null=True)
    country = models.CharField(max_length=50,null=True)
    country_code = models.CharField(max_length=6,null=True)
    country_prefix = models.CharField(max_length=6,null=True)
    international_number =models.CharField(max_length=20,null=True)
    local_number = models.CharField(max_length=20,null=True)
    e164 = models.CharField(max_length=20,null=True)
    carrier = models.CharField(max_length=500,null=True)
# model for the user and link the phone_details and email_details model using foreignkey
class user(models.Model):
    username = models.CharField(max_length=100)
    password = models.TextField(max_length=100)
    number = models.TextField(max_length=20)
    email = models.EmailField(max_length=100)
    email_detail = models.ForeignKey(email_details, on_delete=models.CASCADE)
    phone_detail = models.ForeignKey(phone_details,on_delete=models.CASCADE)