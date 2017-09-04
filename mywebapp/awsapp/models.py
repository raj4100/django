from django.db import models
from django.forms import ModelForm

class Employee(models.Model):
    fname = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50, primary_key = True )
    password = models.CharField(max_length = 50)
    mobile = models.CharField(max_length = 10)

    class Meta:
        db_table = "Employee"

class SignUpForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['fname','email','password','mobile']

class Credentials(models.Model):
    email = models.CharField(max_length = 50, primary_key = True)
    accountid =  models.CharField(max_length = 200)
    accesskey =  models.CharField(max_length = 200)

    class Meta:
        db_table = "Credentials"


class KeyForm(ModelForm):
    class Meta:
        model = Credentials
        fields = ['accountid','accesskey']
