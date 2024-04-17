import model.models as models


def validateId(Hos, id):
    for Patient in Hos.patients:
        if str(Patient.id) == str(id):
            return Patient
    return None

def CreatePatient(Hospital,id,fullname,gender,email,phonenumber,birthdate,address,Contactname,patientrelationship,insuranceCompany,policynumber,statePolicy,policyValidity):
     patient = validateId(Hospital, id)
     if patient:
      raise Exception ("Ya existe un paciente con esa cedula registrada")
     patient = models.Patient(id,fullname,gender,email,phonenumber,birthdate,address,Contactname,patientrelationship,insuranceCompany,policynumber,statePolicy,policyValidity)
     Hospital.patients.append(patient)
     Hospital.clinicalHistory[str(id)]={}
     print("Paciente: {} creado con éxito".format(patient.fullname))

def updatePatientById(Hos, id, new_fullname, new_gender, new_email, new_phonenumber, new_birthdate, new_address, new_contact_name, new_patient_relationship, new_insurance_company, new_policy_number, new_state_policy, new_policy_validity):
    patient = validateId(Hos, id)
    if patient:
        # Actualizar los datos del paciente
        patient.fullname = new_fullname
        patient.gender = new_gender
        patient.email = new_email
        patient.phonenumber = new_phonenumber
        patient.birthdate = new_birthdate
        patient.address = new_address
        patient.Contactname = new_contact_name
        patient.patientrelationship = new_patient_relationship
        patient.insuranceCompany = new_insurance_company
        patient.policynumber = new_policy_number
        patient.statePolicy = new_state_policy
        patient.policyValidity = new_policy_validity

        print(f"Datos del paciente con cédula {id} actualizados con éxito.")
    else:
        raise Exception(f"No existe un paciente con la cédula {id}")


def scheduleAppointment(Hos, patient_id, date, time, doctor):
    patient = validateId(Hos, patient_id)

    if patient:
        appointment = models.MedicalAppointment(date, time, doctor)
        Hos.appointments.append(appointment) 
        print(f"Cita programada para el paciente {patient.fullname} el {date} a las {time} con el Dr. {doctor}")
    else:
        raise Exception("No existe un paciente con esa cédula")
    

def listPatients(Hospital):
    for Patient in Hospital.patients:
        print(f"ID: {Patient.id}, Nombre: {Patient.fullname}")


def getPatientById(Hospital, id):
    for Patient in Hospital.patients:
        if str(Patient.id) == str(id):
            return Patient
    return None



