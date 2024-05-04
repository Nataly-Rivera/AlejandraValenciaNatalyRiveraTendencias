from django.shortcuts import render
from django.shortcuts import render
from django.views import View
import HospitalApp.validator.patientTypeValidators as patientValidator
import HospitalApp.validator.DoctorValidator as DoctorValidator
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json

# Create your views here.
def validateRol(role,validateRoles):
    if role not in validateRoles:
        raise Exception("rol no valido")
    
    
class patientView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,id=None):
        try:
            token = request.META.get('HTTP_TOKEN')
            sesion = DoctorValidator.getSession(token)
            rol=sesion.user.rol
            validateRol(rol,["Veterinario"])
            if id:
                patient=patientValidator.getpatient(id)
            else:
                patient = patientValidator.getpatients()
            message="registros encontrados"
            status=200
            response={"message":message,"patient":patient}
        except Exception as error:
            message=str(error)
            status=404
            response={"message":message}
        return JsonResponse(response,status=status) 

    def post(self,request):
        
        try:
            body = json.loads(request.body)
            id=body["id"]
            fullname=body["fullname"]
            gender=body["gender"]
            email=body["email"]
            phonenumber=body["phonenumber"]
            birthdate=body["birthdate"]
            address=body["address"]
            Contactname=body["Contactname"]
            patientrelationship=body["patientrelationship"]
            insuranceCompany=body["insuranceCompany"]
            policynumber=body["policynumber"]
            statePolicy=body["statePolicy"]
            policyValidity=body["policyValidity"]
            patientValidator.createpatient(id,fullname,gender,email,phonenumber,birthdate,birthdate,address,Contactname,patientrelationship,insuranceCompany,policynumber,statePolicy,policyValidity)
            message="paciente creada"
            status=200
        except Exception as error:
            message=str(error)
            status=400
        response = {"message":message}
        return JsonResponse(response,status=status) 

    def put(self,request,id):
        try:
            body = json.loads(request.body)
            name=body["name"]
            patientValidator.modifypatient(id,name)
            message="paciente actualizado"
            status=200
        except Exception as error:
            message=str(error)
            status=400
        response = {"message":message}
        return JsonResponse(response,status=status)
    def delete(self,request):
        pass

class OwnerView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,id=None):
        pass
    def post(self,request):
        
        try:
            body=json.loads(request.body)
            DoctorValidator.createOwner(body["name"],body["id"],body["age"])
            message="se ha creado el Doctor exitosamente"
            status=204
        except Exception as error:
            message=str(error)
            status=400
        response = {"message":message}
        return JsonResponse(response,status=status) 

    def put(self,request):
        pass

    def delete(self,request):
        pass

class LoginView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self,request):
        try:
            body=json.loads(request.body)
            session =DoctorValidator.login(body["username"],body["password"])
            message="loguin exitoso"
            status=200
            response = {"message":message,"token":session.token}
        except Exception as error:
            message=str(error)
            status=400
            response = {"message":message}
        return JsonResponse(response,status=status)
    
    def get(self,request):
        try:
            token = request.META.get('HTTP_TOKEN')
            sesion = DoctorValidator.getSession(token)
            rol=sesion.user.rol
            status=200
            message = "token encontrado"
            rol=sesion.user.rol
        except Exception as error:
            message = str(error)
            status = 400
            rol=None
        response = {"message":message, "rol": rol}
        return JsonResponse(response,status=status)
