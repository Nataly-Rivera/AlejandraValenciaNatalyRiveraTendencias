from .typeValidator import *
import services.PersonalAdminService as PersonalAdminService
from services import PersonalAdminService

def createPatient(Hos,rol):
    fullname=input("Ingrese nombre del " + rol + ":")
    textValidator(fullname,"nombre de " + rol + ":")
    id=numberValidator(input("Ingrese la cedula de " + rol + ":"), "cedula de " + rol + ":")
    gender=input("Ingrese genero del " + rol + ":")
    textValidator(fullname,"genero de " + rol + ":")
    email=validateEmail(input("Ingrese correo electronico del " + rol + ":"))
    textValidator(fullname,"correo electronico de " + rol + ":")
    phonenumber=validatePhone(input("Ingrese numero de telefono del " + rol + ":"))
    textValidator(fullname,"numero telefono de " + rol + ":")
    birthdate=validatebirthdate(input("Ingrese fecha de nacimiento del " + rol + "(DD/MM/AA)" + ":"))
    textValidator(fullname,"fecha de nacimiento del " + rol + ":")
    address=validateAddress(input("Ingrese direccion del " + rol + ":"))
    textValidator(fullname,"direccion de " + rol + ":")
    Contactname=input("Ingrese nombre del acompañante " + ":")
    textValidator(fullname,"nombre del acompañante " + rol + ":")
    patientrelationship=input("Ingrese relacion del acompañante " + ":")
    textValidator(fullname,"relacion del acompañante " + rol + ":")
    insuranceCompany=input("Ingrese compañia de seguros del " + rol + ":")
    textValidator(fullname,"compañia de seguros " + rol + ":")
    policynumber=input("Ingrese numero de poliza del " + rol + ":")
    textValidator(fullname,"numero poliza de " + rol + ":")
    statePolicy=input("Ingrese el estado de poliza del " + rol + ":")
    textValidator(fullname,"estado de poliza " + rol + ":")
    policyValidity=input("Ingrese vigencia de poliza del " + rol + ":")
    textValidator(fullname,"vigencia de poliza del" + rol + ":")
    PersonalAdminService.CreatePatient(Hos,id,fullname,gender,email,phonenumber,birthdate,address,Contactname,patientrelationship,insuranceCompany,policynumber,statePolicy,policyValidity)

def updatePatient(Hos, id):
    patient = PersonalAdminService.validateId(Hos, id)
    if patient:
        
        new_fullname = input(f"Ingrese el nuevo nombre completo para el paciente {patient.fullname}: ")
        new_gender = input(f"Ingrese el nuevo género para el paciente {patient.fullname}: ")
        new_email = input(f"Ingrese el nuevo correo electrónico para el paciente {patient.fullname}: ")
        new_phonenumber = input(f"Ingrese el nuevo numero de telefono para el paciente {patient.fullname}: ")
        new_birthdate = input(f"Ingrese la nueva fecha de nacimiento para el paciente {patient.fullname}: ")
        new_address = input(f"Ingrese la nueva direccion para el paciente {patient.fullname}: ")
        new_contactname = input(f"Ingrese el nuevo nombre de contacto de emergencia para el paciente {patient.fullname}: ")
        new_patientrelationship = input(f"Ingrese la nueva relacion para el paciente {patient.fullname}: ")
        new_insurancecompany = input(f"Ingrese la nueva compañia de seguros para el paciente {patient.fullname}: ")
        new_policynumber = input(f"Ingrese el nuevo numero de la poliza para el paciente {patient.fullname}: ")
        new_statepolicy = input(f"Ingrese el nuevo estado de la poliza para el paciente {patient.fullname}: ")
        new_policyvalidity = input(f"Ingrese la nueva fecha de vigencia de la poliza para el paciente {patient.fullname}: ")
        
        PersonalAdminService.updatePatientById(
            Hos, id, new_fullname, new_gender, new_email, new_phonenumber, new_birthdate, new_address, new_contactname,
            new_patientrelationship, new_insurancecompany, new_policynumber, new_statepolicy, new_policyvalidity
        )
    else:
        raise Exception(f"No existe un paciente registrado con la cédula {id}")

def scheduleAppointment(Hos, rol="Paciente"):
    patient_id = numberValidator(input(f"Ingrese la cédula del {rol}: "), f"Cédula de {rol}")
    date = input("Ingrese la fecha de la cita (DD/MM/YYYY): ")
    time = input("Ingrese la hora de la cita: ")
    doctor = input("Ingrese el nombre del doctor: ")

    PersonalAdminService.scheduleAppointment(Hos, patient_id, date, time, doctor)


def listAllPatients(Hos):
    PersonalAdminService.listPatients(Hos)



