from django.shortcuts import render, redirect
from .models import PatientData
from .forms import PatientDataForm


def data_input(request):
    context = {}
    if request.method == 'POST':
        patient_data_form = PatientDataForm(request.POST)

        # Check for duplicate entries
        existing_entry = PatientData.objects.filter(
            name=patient_data_form.data['name'], 
            mobile=patient_data_form.data['mobile'], 
            gender=patient_data_form.data['gender'], 
            age=patient_data_form.data['age']
        ).exists()

        if existing_entry:
            context['duplicate_entry'] = True
        elif patient_data_form.is_valid():
            context['form'] = PatientDataForm()
            context['form_submitted'] = True
            patient_data_form.save()
            return render(request, 'data_input.html', context)



    else:
        patient_data_form = PatientDataForm()


    context = {
        'patient_data_form': patient_data_form,
    }

    return render(request, 'data_input.html', context)

def home(request):
    return render(request, 'datainput/index.html')