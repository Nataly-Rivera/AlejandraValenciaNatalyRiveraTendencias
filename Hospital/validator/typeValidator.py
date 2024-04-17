import re


def textValidator(string,element):
    if string==None or string=="":
        raise Exception(element + "no es un valor valido")

def numberValidator(string,element):
    textValidator(string,element)
    try:
        return int(string)
    except:
        raise Exception(element + " no es un numero valido")
    

def assignrole(role):
    roleSelection = {
    "1": "adminRH",
    "2": "PersonalAdmin",
    "3": "doctor",
    "4": "Enfermera",
    }
    return roleSelection.get(role, "Opción inválida")


def costValidator(cost, element):
    try:
        cost = cost.replace('.', '').replace(',', '')
        cost = float(cost)
        if cost <= 0:
            raise ValueError
    except ValueError:
        raise ValueError(element + "El costo ingresado no es valido.")
    return cost

#-------- RESTRICCIONES DE REGISTRO---------#

def validateEmail(email):
    while True:
        try:
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                raise ValueError("Correo inválido. Debe tener un formato válido.")

            if not re.match(r"[^@]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$", email):
                raise ValueError("Correo inválido. El dominio no es válido.")
            
            return email
        except ValueError as e:
            print(str(e))
            email = input("Ingrese correo electrónico nuevamente: ")

def validatePhone(phone):
    while True:
        try:
            if not re.match(r"^\d{1,10}$", phone):
                raise ValueError("Número de teléfono inválido. Debe contener entre 1 y 10 dígitos.")
            return phone
        except ValueError as e:
            print(str(e))
            phone = input("Ingrese número de teléfono nuevamente: ")

def validatebirthdate(birthdate):
    while True:
        try:
           
            if not re.match(r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/\d{4}$", birthdate):
                raise ValueError("Formato de fecha de nacimiento inválido. Debe ser DD/MM/YYYY.")

            return birthdate
        except ValueError as e:
            print(str(e))
            birthdate = input("Ingrese fecha de nacimiento nuevamente (DD/MM/YYYY): ")


def validateAddress(address):
    while True:
        try:
          
            if len(address) > 30:
                raise ValueError("Dirección inválida. Debe tener máximo 30 caracteres.")
            
            return address
        except ValueError as e:
            print(str(e))
            address = input("Ingrese dirección nuevamente: ")

def validateuserName(username):
    while True:
        try:
           
            if len(username) > 15:
                raise ValueError("Nombre de usuario no valido. Debe tener máximo 15 caracteres.")
            if not username.isalnum():
                raise ValueError("Nombre de usuario no valido. Solo debe contener letras y números.")
            
            return username
        except ValueError as e:
            print(str(e))
            username = input("Ingrese usuario nuevamente: ")

def validatePassword(password):
    while True:
        try:
            if len(password) < 8:
                raise ValueError("Contraseña inválida. Debe tener al menos 8 caracteres.")
            if not re.search(r"[A-Z]", password):
                raise ValueError("Contraseña inválida. Debe incluir al menos una mayúscula.")
            if not re.search(r"\d", password):
                raise ValueError("Contraseña inválida. Debe incluir al menos un número.")
            if not re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?/~\\-]", password):
                raise ValueError("Contraseña inválida. Debe incluir al menos un carácter especial.")
            return password
        except ValueError as e:
            print(str(e))
            password = input("Ingrese contraseña nuevamente: ")


