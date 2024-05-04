
class Patient():
    def __init__(self,id,fullname,gender,email,phonenumber,birthdate,address,Contactname,patientrelationship,insuranceCompany,policynumber,statePolicy,policyValidity):
        self.id=id
        self.fullname=fullname
        self.gender=gender
        self.email=email
        self.phonenumber=phonenumber
        self.birthdate=birthdate
        self.address=address
        self.Contactname=Contactname
        self.patientrelationship=patientrelationship
        self.insuranceCompany=insuranceCompany
        self.policynumber=policynumber
        self.statePolicy=statePolicy
        self.policyValidity=policyValidity


class Employee():
    def __init__(self,id,fullname,email,phonenumber,birthdate,address,rol,username,password):
        self.id=id
        self.fullname=fullname
        self.email=email
        self.phonenumber=phonenumber
        self.birthdate=birthdate
        self.address=address
        self.rol=rol
        self.username=username
        self.password=password


class Order():
    def __init__(self,id,patientId,doctorId,date,diagnosticHelp,medicines,procedure):
        self.id=id
        self.patientId=patientId
        self.doctorId=doctorId
        self.date=date
        self.medicines = medicines
        self.procedure = procedure
        self.diagnosticHelp = diagnosticHelp


class Invoice():
    def __init__(self,id,patientId,patientname,patientage,doctorname,insuranceCompany,daysvalidity,policyEndDate):
        self.id=id
        self.patientId=patientId
        self.patientage=patientage
        self.patientname=patientname
        self.doctorname=doctorname
        self.insuranceCompany=insuranceCompany
        self.daysvalidity=daysvalidity
        self.policyEndDate=policyEndDate
        
class MedicalAppointment():
    def __init__(self, idPatient, idDoctor, date):
        self.id = idPatient
        self.idPatient = idPatient
        self.idDoctor = idDoctor
        self.date = date

class Medicine():
    def __init__(self,orderId,itemMedicine,medicineName,medicineDose,durationMedication,medicineCost):       
        self.orderId = orderId
        self.itemMedicine = itemMedicine
        self.medicineName = medicineName
        self.medicineDose = medicineDose
        self.durationMedication = durationMedication
        self.medicineCost = medicineCost


class Procedure():
    def __init__(self,orderId,itemProcedure,nameProcedure,numberRepeated,frequencyRepeated,procedureCost,requiresSpecialistP,specialistId):
        self.orderId = orderId
        self.itemProcedure = itemProcedure
        self.nameProcedure = nameProcedure
        self.numberRepeated = numberRepeated
        self.frequencyRepeated = frequencyRepeated
        self.procedureCost = procedureCost
        self.requiresSpecialistP = requiresSpecialistP
        self.specialistId = specialistId                    


class DiagnosticHelp():
    def __init__(self, orderId, itemDiagnostic, nameDiagnostic,quantity, diagnosticCost, requiresSpecialistD, specialistId):
        self.orderId = orderId
        self.itemDiagnostic = itemDiagnostic
        self.nameDiagnostic = nameDiagnostic
        self.quantity = quantity
        self.diagnosticCost = diagnosticCost
        self.requiresSpecialistD = requiresSpecialistD
        self.specialistId = specialistId


class Hospital():
    def __init__(self):
        self.employees=[]
        self.patients=[]
        self.orders=[]
        self.invoices=[]
        self.appointments=[]
        self.medicines = []
        self.diagnosticHelp = []
        self.procedures = []
        self.visitsHistory = {}   
        self.clinicalHistory={}