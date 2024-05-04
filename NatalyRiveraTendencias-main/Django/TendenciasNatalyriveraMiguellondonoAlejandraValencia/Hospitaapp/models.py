from django.db import models

class Patient(models.Model):
    id=models.BigIntegerField(primary_key=True)
    fullname=models.CharField(max_length=30)
    gender=models.CharField()
    email=models.EmailField()
    phonenumber=models.IntegerField(max_lenght=20)
    birthdate=models.DateField()
    address=models.CharField(max_length=255)
    Contactname=models.CharField()
    patientrelationship=models.CharField()
    insuranceCompany=models.CharField()
    policynumber=models.IntegerField()
    statePolicy=models.CharField()
    policyValidity=models.DateField()


# Create your models here.
