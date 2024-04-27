from django.db import models

# Create your models here.
class Patient(models.Model):
    id=models.BigIntegerField(primary_key=True)
    fullname=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    email=models.EmailField()
    phonenumber=models.IntegerField()
    birthdate=models.DateField()
    address=models.CharField(max_length=255)
    Contactname=models.CharField(max_length=20)
    patientrelationship=models.CharField(max_length=100)
    insuranceCompany=models.CharField(max_length=100)
    policynumber=models.IntegerField()
    statePolicy=models.CharField(max_length=50)
    policyValidity=models.DateField()


class Employee(models.Model):
    id=models.BigIntegerField (primary_key=True)
    email=models.EmailField()
    phonenumber=models.IntegerField()
    birthdate=models.DateField()
    address=models.CharField(max_length=255)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    patient_id = models.BigIntegerField()
    doctor_id = models.BigIntegerField()
    date = models.DateField()
    medicines = models.TextField()
    procedure = models.TextField()
    
class Invoice (models.Model):
    patient_id = models.BigIntegerField(primary_key=True)
    patient_age = models.IntegerField()
    patient_name = models.CharField(max_length=255)
    doctor_name = models.CharField(max_length=255)
    insurance_company = models.CharField(max_length=255)
    days_validity = models.IntegerField()
    policy_end_date = models.DateField()

class MedicalAppointment(models.Model):
    id=models.BigIntegerField (primary_key=True)
    idPatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    idDoctor = models.BigIntegerField()
    date = models.DateField()

class Medicine(models.Model):
    orderid = models.BigIntegerField(primary_key=True)
    itemMedicine = models.CharField(max_length=255)
    medicineName = models.CharField(max_length=255)
    medicineDose = models.CharField(max_length=100)
    durationMedication = models.CharField(max_length=100)
    medicineCost = models.DecimalField(max_digits=10, decimal_places=2)
   
class Procedure(models.Model):
    orderId = models.BigIntegerField(primary_key=True)
    itemProcedure = models.CharField(max_length=255)
    nameProcedure = models.CharField(max_length=255)
    numberRepeated = models.IntegerField()
    frequencyRepeated = models.CharField(max_length=100)
    procedureCost = models.DecimalField(max_digits=10, decimal_places=2)
    requiresSpecialistP = models.BooleanField()
    specialistId = models.BigIntegerField(null=True, blank=True)

class DiagnosticHelp(models.Model):
    orderId = models.BigIntegerField(primary_key=True)
    itemDiagnostic = models.CharField(max_length=255)
    nameDiagnostic = models.CharField(max_length=255)
    quantity = models.IntegerField()
    diagnosticCost = models.DecimalField(max_digits=10, decimal_places=2)
    requiresSpecialistD = models.BooleanField()
    specialistId = models.BigIntegerField(null=True, blank=True)

class Hospital(models.Model):
    employees = models.JSONField(default=list)
    patients = models.JSONField(default=list)
    orders = models.JSONField(default=list)
    invoices = models.JSONField(default=list)
    appointments = models.JSONField(default=list)
    medicines = models.JSONField(default=list)
    diagnosticHelp = models.JSONField(default=list)
    procedures = models.JSONField(default=list)
    visitsHistory = models.JSONField(default=dict)
    clinicalHistory = models.JSONField(default=dict)

class Session(models.Model):
    id=models.AutoField(primary_key=True)
    token=models.CharField(max_length=200)
    user=models.ForeignKey(Patient, on_delete=models.CASCADE)

