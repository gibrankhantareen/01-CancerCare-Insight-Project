from django import forms
from .models import Patient, Treatment, Outcome, Cost

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = '__all__'

class OutcomeForm(forms.ModelForm):
    class Meta:
        model = Outcome
        fields = '__all__'

class CostForm(forms.ModelForm):
    class Meta:
        model = Cost
        fields = '__all__'

