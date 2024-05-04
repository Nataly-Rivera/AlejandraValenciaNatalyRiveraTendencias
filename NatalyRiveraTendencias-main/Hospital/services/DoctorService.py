import datetime
import model.models as models

def validateId(Hospital,id):
    for Patient in Hospital.patients:
        if Patient.id==id:
            return Patient
    return None

def validateIdExist(Hospital,id):
    for Patient in Hospital.patients:
        if Patient.id==id:
            return id
    return None



def createMedicalHistoryQuery(Hospital,patientId,doctorId,consultationReason,symptomatology,diagnosis,order):
    patient = validateId(Hospital,patientId)
    if not patient:
        raise Exception("No existe el paciente")
    newClinicalHistory ={}
    date = datetime.datetime.today()
    newClinicalHistory["doctorId"]=doctorId
    newClinicalHistory["consultationReason"]=consultationReason
    newClinicalHistory["symptomatology"]=symptomatology
    newClinicalHistory["diagnosis"]=diagnosis
    newClinicalHistory["order"]=order     
    Hospital.clinicalHistory[str(patientId)][date] = newClinicalHistory
  
def getHistoryClinicQuery(hospital, patientId):
    patient = validateId(hospital, patientId)
    if not patient:
        raise Exception("No existe el paciente.")

    patient_history = hospital.clinicalHistory.get(str(patientId))
    if not patient_history:
        raise Exception("No hay historial clínico registrado para este paciente.")

    return patient_history



def createOrder(Hospital, orderId, patientId, doctorId,date,diagnosticHelp,medicines,procedure):
    patientId = validateIdExist(Hospital,patientId)
    if not patientId:
        raise Exception("no existe el paciente")   
    order= models.Order(orderId, patientId, doctorId,date,diagnosticHelp,medicines,procedure) 
    Hospital.orders.append(order)
    return order 
    
     
def createMedicine(Hospital,orderId, itemMedicine, medicineName, medicineDose, durationMedication, medicineCost):
    medicine = models.Medicine(orderId, itemMedicine, medicineName, medicineDose, durationMedication, medicineCost)
    Hospital.medicines.append(medicine)
    return medicine
   


def createProcedure(Hospital,orderId,itemProcedure,nameProcedure,numberRepeated,frequencyRepeated,procedureCost,requiresSpecialistP,specialistId):
    procedure = models.Procedure(orderId,itemProcedure,nameProcedure,numberRepeated,frequencyRepeated,procedureCost,requiresSpecialistP,specialistId)
    Hospital.procedures.append(procedure)
    return procedure

    
def createDiagnosticHelp(Hospital,orderId, itemDiagnostic, nameDiagnostic, quantity, diagnosticCost, requiresSpecialistD, specialistId):
    diagnosticHelp = models.DiagnosticHelp(orderId,itemDiagnostic, nameDiagnostic, quantity, diagnosticCost, requiresSpecialistD, specialistId)
    Hospital.diagnosticHelp.append(diagnosticHelp)
    return diagnosticHelp
    