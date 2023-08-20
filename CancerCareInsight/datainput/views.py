from django.shortcuts import render, redirect
from .forms import PatientForm, TreatmentForm, OutcomeForm, CostForm

def data_input(request):
    if request.method == 'POST':
        p_form = PatientForm(request.POST)
        t_form = TreatmentForm(request.POST)
        o_form = OutcomeForm(request.POST)
        c_form = CostForm(request.POST)

        if p_form.is_valid() and t_form.is_valid() and o_form.is_valid() and c_form.is_valid():
            patient = p_form.save()
            t_form.instance.patient = patient
            t_form.save()
            o_form.instance.patient = patient
            o_form.save()
            c_form.instance.patient = patient
            c_form.save()
            return redirect('home')  # Redirect to homepage after successful submission

    else:
        p_form = PatientForm()
        t_form = TreatmentForm()
        o_form = OutcomeForm()
        c_form = CostForm()

    context = {
        'p_form': p_form,
        't_form': t_form,
        'o_form': o_form,
        'c_form': c_form,
    }
    return render(request, 'datainput/data_input.html', context)


def home(request):
    return render(request, 'datainput/index.html')
