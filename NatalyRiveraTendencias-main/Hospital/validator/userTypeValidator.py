from .typeValidator import *
import validator.typeValidator as typeValidator
import services.HumanResourcesService as HumanResourcesService
import services.loginService as loginService


def createEmployee(Hos,rol):
    fullname=input("Ingrese nombre completo del " + rol + ":")
    textValidator(fullname,"nombre de " + rol+ ":")
    id=numberValidator(input("Ingrese la cedula de " + rol + ":"), "cedula de " + rol +":")
    email= validateEmail(input("Ingrese correo electronico del " + rol + ":"))
    textValidator(fullname,"correo electronico de " + rol + ":")
    phonenumber=validatePhone(input("Ingrese numero de telefono del " + rol + ":"))
    textValidator(fullname,"numero telefono de " + rol + ":")
    birthdate=validatebirthdate(input("Ingrese fecha de nacimiento del " + rol + "(DD/MM/AA)" + ":"))
    textValidator(fullname,"fecha de nacimiento de " + rol + ":")
    address=validateAddress(input("Ingrese direccion del " + rol + ":"))
    textValidator(fullname,"direccion de " + rol + ":")
    rol="opcion invalida"
    while rol == "opcion invalida":
        print("Selecciona el rol del empleado:")
        rol=input("1.adminRH\n2.PersonalAdmin\n3.doctor\n4.Enfermera\n")
        rol=typeValidator.assignrole(rol)
    username=validateuserName(input("Ingrese usuario del " + rol + ":"))
    textValidator(username,"usuario de " + rol + ":")
    password=validatePassword(input("Ingrese contraseña del " + rol + ":"))
    textValidator(password,"contraseña de " + rol + ":")
    HumanResourcesService.createEmployee(Hos,id,fullname,email,phonenumber,birthdate,address,rol,username,password)
    
def deleteUser(Hos, rol="empleado"):
    id = numberValidator(input(f"Ingrese la cédula del empleado a eliminar: "), f"Cédula de emplead")
    HumanResourcesService.deleteEmployee(Hos, id)
   
def updateEmployee(Hos, user):
    textValidator(user.fullname, f"Nombre de {user.fullname}")
    textValidator(user.email, f"Correo electrónico de {user.fullname}")
    textValidator(user.phonenumber, f"Número de teléfono de {user.fullname}")
    textValidator(user.birthdate, f"fecha de nacimiento de {user.fullname} ")
    textValidator(user.address, f"direccion de {user.fullname} ")
    textValidator(user.username, f"nombre de usuario de {user.fullname} ")
    textValidator(user.password, f"contraseña de {user.fullname} ")
    HumanResourcesService.updateEmployee(Hos, user)
    
def listAllEmployees(Hos):
    HumanResourcesService.listEmployees(Hos)