from services import NurseService
from validator.typeValidator import *



def createHistoryVisitsQuery(Hospital,id):
    patientId = id

    bloodPressure = input("ingrese la presion arterial del paciente \n")
    textValidator(bloodPressure,"presion arterial")
    temperature = input("ingrese la temperatura del paciente\n")
    textValidator(temperature,"la temperatura")
    pulse =input("ingrese el pulso \n")
    textValidator(pulse,"pulso")
    oxygenInBlood = input("ingrese el nivel de oxigeno en la sangre del paciente \n")
    textValidator(oxygenInBlood,"ingrese el nivel de oxigeno en la sangre")
    medicine=input("ingrese el medicamento a recetar\n")
    if medicine=="":
        medicine="N/A"
    textValidator(medicine,"ingrese el medicamento")
    medicineDosage=input("dosis de medicamento\n")
    if medicineDosage=="":
        medicineDosage="N/A"
    procedure=input("ingrese el procedimiento\n")
    if procedure=="":
        procedure="N/A"
    textValidator(procedure,"procedimiento")
    DetailofProcedure=input("detalle del procedimiento \n")
    if DetailofProcedure=="":
        DetailofProcedure="N/A"
    textValidator(DetailofProcedure,"detalle del procedimiento")    
    medicaltests = input("Pruebas medicas realizadas\n")
    textValidator(medicaltests,"pruebas medicas")
    observations = input("observaciones \n")
    if observations=="":
       observations="N/A"
    textValidator(observations,"observaciones")   
    NurseService.createHistoryVisitsQuery(Hospital,patientId,bloodPressure,temperature,pulse,oxygenInBlood,medicine,medicineDosage,procedure,DetailofProcedure,medicaltests,observations)
 



def getHistoryVisitsQuery(Hospital, patientId):
    NurseService.getHistoryVisitsQuery(Hospital,patientId)
    patient_history = Hospital.visitsHistory.get(str(patientId))
    print("Historial de visitas del paciente:")
    for visit_date, visitdetails in patient_history.items():
        print(f"Fecha de visita: {visit_date}")
        for key, value in visitdetails.items():
            print(f"{key}: {value}")
        print("")