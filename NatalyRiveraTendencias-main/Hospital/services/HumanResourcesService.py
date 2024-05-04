import model.models as models
def validateId(Hos,id):
    for Employee in Hos.employees:
        if Employee.id==id:
            return Employee
    return None
def validateUserName(Hos,username):
    for Employee in Hos.employees:
        if Employee.username==username:
            return Employee
    return None

def createEmployee(Hos, id, fullname, email, phonenumber, birthdate, address, rol, username, password):
    user = validateId(Hos, id)
    if user:
        raise Exception("Ya existe un usuario con esa cédula registrada")
    user = validateUserName(Hos, username)
    if user:
        raise Exception("Ya existe un usuario con ese username registrado")

    user = models.Employee(id, fullname, email, phonenumber, birthdate, address, rol, username, password)
    Hos.employees.append(user)
    print("Empleado: {} creado con éxito".format(user.fullname))

def deleteEmployee(Hos, id):
    user = validateId(Hos, id)
    if user:
        Hos.employees.remove(user)
        print(f"Empleado: {user.fullname} con cédula {id} ha sido eliminado exitosamente")
    else:
        raise Exception("No existe un usuario con esa cédula")
    

 
def updateEmployee(Hos, user):
    Newfullname = input(f"Ingrese el nuevo nombre completo para {user.fullname}: ")
    Newemail = input(f"Ingrese el nuevo correo electrónico para {user.fullname}: ")
    Newphonenumber = input(f"Ingrese el nuevo número de teléfono para {user.fullname}: ")
    NewBirthdate=input(f"Ingrese la nueva fecha de nacimiento para {user.fullname}: ")
    Newaddress=input(f"Ingrese la nueva direccion para {user.fullname}: ")
    Newusername=input(f"Ingrese el nuevo nombre de usuario para {user.fullname}: ")
    Newpassword=input(f"Ingrese la nueva contraseña para {user.fullname}: ")
    user.fullname = Newfullname
    user.email = Newemail
    user.phonenumber = Newphonenumber
    user.birthdate = NewBirthdate
    user.address = Newaddress
    user.username = Newusername
    user.password = Newpassword
    print(f"Datos de {user.fullname} actualizados con éxito.")
    
def listEmployees(Hospital):
    for Employee in Hospital.employees:
        print(f"ID: {Employee.id}, Nombre: {Employee.fullname}, Rol: {Employee.rol}")


def getEmployeeById(Hospital, id):
    for Employee in Hospital.employees:
        if Employee.id == id:
            return Employee
    return None