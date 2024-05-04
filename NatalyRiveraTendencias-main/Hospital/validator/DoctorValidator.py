import validator.typeValidator as val
from services import DoctorService
import datetime


def createMedicalHistoryQuery(Hospital, patientId, doctorId):
    
    consultationReason = input("Ingrese la razón o motivo de la consulta: ")
    val.textValidator(consultationReason, "razón de la consulta")
    symptomatology = input("Ingrese los síntomas: ")
    val.textValidator(symptomatology, "los síntomas")
    order = createOrder(Hospital, patientId, doctorId)
    orderp = vars(order)
    print(orderp)
    if not orderp.get('diagnosticHelp'):
        diagnosis = input("Ingrese el diagnóstico: ")
        val.textValidator(diagnosis, "diagnóstico")
    else:
        diagnosis = "N/A"

    DoctorService.createMedicalHistoryQuery(Hospital, patientId, doctorId, consultationReason, symptomatology, diagnosis, orderp)

def getHistoryClinicQuery(hospital, patientId):
    patientHistory = DoctorService.getHistoryClinicQuery(hospital, patientId)
    print("Historial clínico del paciente:")
    for visitDate, visitDetails in patientHistory.items():
        printVisitDetails(visitDate, visitDetails)

def printVisitDetails(visitDate, visitDetails):
    print(f"Fecha: {visitDate}")
    print(f"Razón de la visita: {visitDetails['consultationReason']}")
    print(f"Síntomas: {visitDetails['symptomatology']}")
    print(f"Diagnóstico: {visitDetails['diagnosis']}")
    printOrderDetails(visitDetails.get('order', {}))
    print("")

def printOrderDetails(orderDetails):
    if orderDetails:
        print("Orden:")
        for key, value in orderDetails.items():
            if key not in ['medicines', 'procedure', 'diagnosticHelp']:
                print(f"  {key}: {value}")
        printMedicines(orderDetails.get('medicines', []))
        printProcedures(orderDetails.get('procedure', []))
        printDiagnosticHelp(orderDetails.get('diagnosticHelp', []))

def printMedicines(medicines):
    if medicines:
        print("Medicamentos:")
        for medicine in medicines:
            print(f"  - Nombre: {medicine['medicineName']}, Dosis: {medicine['medicineDose']}, Duración: {medicine['durationMedication']}, Costo: {medicine['medicineCost']}")

def printProcedures(procedures):
    if procedures:
        print("Procedimientos:")
        for procedure in procedures:
            print(f"  - Nombre: {procedure['nameProcedure']}, Repetición: {procedure['numberRepeated']}, Frecuencia: {procedure['frequencyRepeated']}, Costo: {procedure['procedureCost']}")

def printDiagnosticHelp(diagnosticHelp):
    if diagnosticHelp:
        print("Ayudas diagnósticas:")
        for diagnostic in diagnosticHelp:
            print(f"  - Nombre: {diagnostic['nameDiagnostic']}, Cantidad: {diagnostic['quantity']}, Costo: {diagnostic['diagnosticCost']}")






#...........
def createOrder(Hospital, patientId, doctorId):
    orderId = len(Hospital.orders)
    date = datetime.date.today()
    procedures = []
    medicines = []
    diagnosticHelp = []

    while True:
        Options()
        option = input("Ingrese el número correspondiente a la opcion que desees: ")

        if option == '1':
            addProcedure(diagnosticHelp, procedures, Hospital, orderId)
        elif option == '2':
            addMedicine(diagnosticHelp, medicines, Hospital, orderId)
        elif option == '3':
            addDiagnosticHelp(procedures, medicines, diagnosticHelp, Hospital, orderId)
        elif option == '4':
            break
        else:
            print("Opción invalida. por favor ingresa el numero que corresponde a cada opcion")

    order = DoctorService.createOrder(Hospital, orderId, patientId, doctorId, date, diagnosticHelp, medicines, procedures)
    return order

def Options():
    print("¿Que deseas hacer?")
    print("Seleccione una opción que requiera el paciente:")
    print("1. Agregar un procedimiento")
    print("2. Agregar una medicina o medicamento")
    print("3. Agregar una ayuda diagnóstica")
    print("4. Finalizar registro medico")

def addProcedure(diagnosticHelp, procedures, Hospital, orderId):
    if diagnosticHelp:
        print("Ya se ha agregado una ayuda diagnóstica. No se pueden agregar procedimientos.")
    else:
        procedure = createProcedure(Hospital, orderId)
        procedures.append(procedure)

def addMedicine(diagnosticHelp, medicines, Hospital, orderId):
    if diagnosticHelp:
        print("Ya se ha agregado una ayuda diagnóstica. No se pueden agregar medicamentos.")
    else:
        medicine = createMedicine(Hospital, orderId)
        medicines.append(medicine)

def addDiagnosticHelp(procedures, medicines, diagnosticHelp, Hospital, orderId):
    if procedures or medicines:
        print("No se puede agregar ayuda diagnóstica, ya se han agregado procedimientos o medicamentos.")
    else:
        diagnostic = createDiagnosticHelp(Hospital, orderId)
        diagnosticHelp.append(diagnostic)




def createMedicine(Hospital,orderId):
    itemMedicine = len(Hospital.medicines) + 1

    medicineName = input("ingrese el nombre de la medicina \n")
    val.textValidator(medicineName,"medicinas")
    medicineDose =input("ingrese la dosis de la medicina \n")
    val.textValidator(medicineDose,"dosis")
    durationMedication = input("ingrese la duracion de la medicacion \n")
    val.textValidator(durationMedication,"duracion ")
    medicineCost = input("ingrese el costo de la medicina \n")
    val.costValidator(medicineCost,"costo")       
    medicine=DoctorService.createMedicine(Hospital,orderId,itemMedicine,medicineName,medicineDose,durationMedication,medicineCost) 
    medicine = vars(medicine)
    print(medicine)
    return medicine

def createProcedure(Hospital,orderId):
    itemProcedure = len(Hospital.procedures) + 1
    nameProcedure = input("ingrese el nombre del procedimiento \n")
    val.textValidator(nameProcedure,"procedimiento")
    numberRepeated =input("ingrese el numero de veces que se repite el procedimiento \n")
    val.textValidator(numberRepeated,"numero")
    frequencyRepeated = input("ingrese la frecuencia que se repite el procedimiento \n")
    val.textValidator(frequencyRepeated,"frecuencia ")
    procedureCost = input("ingrese el costo del procedimiento \n")
    val.costValidator(procedureCost,"costo")   
    requiresSpecialistP = input("requiere especialista? (si/no) \n")
    val.textValidator(requiresSpecialistP,"especialista ")
    if requiresSpecialistP.lower() == 'si':
        specialistId = input("Ingrese el ID del especialista: ")
        val.numberValidator(specialistId,"id especialista")      
    else:
         requiresSpecialistP= "no"
         specialistId = "N/A"
    procedure=DoctorService.createProcedure(Hospital,orderId,itemProcedure,nameProcedure,numberRepeated,frequencyRepeated,procedureCost,requiresSpecialistP,specialistId)
    procedure = vars(procedure)
    print(procedure)
    return procedure 
    
def createDiagnosticHelp(Hospital, orderId):
 
    itemDiagnostic = len(Hospital.diagnosticHelp) + 1
    nameDiagnostic = input("Ingrese el nombre del diagnóstico:\n ")
    val.textValidator(nameDiagnostic, "nombre del diagnóstico")
    quantity = input("Ingrese la cantidad del diagnóstico:\n")
    val.textValidator(quantity, "cantidad del diagnóstico")
    diagnosticCost = input("Ingrese el costo del diagnóstico: \n")
    val.costValidator(diagnosticCost, "costo del diagnóstico")
    requiresSpecialistD = input("¿Requiere un especialista para el diagnóstico? (Si/no):\n ").lower()
    val.textValidator(requiresSpecialistD, "especialista para el diagnóstico")
    if requiresSpecialistD == 'si':
        specialistId = input("Ingrese el ID del especialista: ")
        val.numberValidator(specialistId,"id especialista")  
    else:
         requiresSpecialistD= "no"
         specialistId = "N/A"   

    diagnosticHelp=DoctorService.createDiagnosticHelp(Hospital,orderId, itemDiagnostic, nameDiagnostic, quantity, diagnosticCost, requiresSpecialistD, specialistId)
    diagnosticHelp = vars(diagnosticHelp)
    print(diagnosticHelp)
    return diagnosticHelp
      