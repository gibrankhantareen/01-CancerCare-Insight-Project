from django.shortcuts import render, redirect
from .models import PatientData
from .forms import PatientDataForm


def data_input(request):
    if request.method == 'POST':
        patient_data_form = PatientDataForm(request.POST)

        if patient_data_form.is_valid():
            patient_data_form.save()
            return redirect('home')  # Redirect to the home page after successful submission

    else:
        patient_data_form = PatientDataForm()


    context = {
        'patient_data_form': patient_data_form,
    }
    print(patient_data_form)

    return render(request, 'data_input.html', context)

def home(request):
    return render(request, 'datainput/index.html')