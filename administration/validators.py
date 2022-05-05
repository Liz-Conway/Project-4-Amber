'''
Created on 27 Apr 2022

@author: liz
'''
from django.views import View
from django.http import JsonResponse
from .models import Diagnosis


class DiagnosisValidator(View):
    '''
    This class checks whether a diagnosis entered onto the Add Diagnosis form
    already exists.
    If the diagnosis already exists then the validation fails,
    otherwise the validation passes.
    '''


    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            # get the diagnosis from the client side.
            diagnosis = request.GET.get("diagnosis", None)
            # check for the diagnosis in the database.
            if Diagnosis.objects.filter(diagnosis = diagnosis).exists():
                # if diagnosis found -> return not a valid new diagnosis
                return JsonResponse({"valid":False}, status = 200)
            else:
                # if diagnosis not found, then administrator can create a new diagnosis.
                return JsonResponse({"valid":True}, status = 200)
    
        return JsonResponse({}, status = 400)

