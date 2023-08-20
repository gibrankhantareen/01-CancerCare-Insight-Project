from django import forms
from .models import PatientData

class PatientDataForm(forms.ModelForm):
    class Meta:
        model = PatientData
        fields = [
            'name', 'age', 'gender', 'cancer_type', 'stage', 'diagnosis_date',
            'treatment_type', 'start_date', 'end_date', 'medication_names',
            'eradicated', 'recurrence', 'side_effects', 'quality_of_life_post_treatment',
            'direct_costs', 'indirect_costs'
        ]
