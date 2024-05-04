import datetime

def validateId(Hospital,id):
    for Patient in Hospital.patients:
        if Patient.id==id:
            return Patient
    return None




def createHistoryVisitsQuery(Hospital,patientId,bloodPressure,temperature,pulse,oxygenInBlood,medicine,medicineDosage,procedure,DetailofProcedure,medicaltests,observations):
    patient = validateId(Hospital,patientId)
    if not patient:
        raise Exception("No existe ese id")
    
    
    newVisitHistory={}
    date = datetime.datetime.today()
    newVisitHistory["bloodPressure"]=bloodPressure
    newVisitHistory["temperature"]=temperature
    newVisitHistory["pulse"]=pulse
    newVisitHistory["oxygenInBlood"]=oxygenInBlood
    if medicine!="N/A":
        newVisitHistory["medicine"]=medicine
        newVisitHistory["medicineDosage"]=medicineDosage 
    if procedure!="N/A":
        newVisitHistory["procedure"]=procedure
        newVisitHistory["DetailofProcedure"]=DetailofProcedure
    newVisitHistory["medicaltests"]= medicaltests 
    if observations!="N/A":
        newVisitHistory["observations"]=observations        
    Hospital.visitsHistory[str(patientId)][date] = newVisitHistory



def getHistoryVisitsQuery(Hospital, patientId):
    patient = validateId(Hospital, patientId)
    if not patient:
        raise Exception("No existe el paciente")
    
    patient_history = Hospital.visitsHistory.get(str(patientId))
    if not patient_history:
        raise Exception("No hay historial de visitas creada para este paciente.")
        
    
    