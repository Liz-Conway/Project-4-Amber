from django.shortcuts import render
from .models import Diagnosis


def get_diagnosis_list(request):
    diagnoses = Diagnosis.objects.all()
    context = {
        "diagnoses": diagnoses
    }
    return render(request, 'admin/getDiagnosis.html', context)
