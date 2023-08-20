from django import forms
from .models import PatientData

class PatientDataForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))
    medication_names = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    eradicated = forms.ChoiceField(choices=[('YES', 'YES'), ('NO', 'NO'), ('MAYBE', 'MAYBE')])
    recurrence = forms.ChoiceField(choices=[('YES', 'YES'), ('NO', 'NO'), ('MAYBE', 'MAYBE')])

    class Meta:
        model = PatientData
        fields = [
            'name', 'age', 'gender', 'cancer_type', 'stage', 'diagnosis_date',
            'treatment_type', 'start_date', 'end_date', 'medication_names',
            'eradicated', 'recurrence', 'side_effects', 'quality_of_life_post_treatment',
            'direct_costs', 'indirect_costs'
        ]

    
        labels = {
            'name': 'Full Name',
            'age': 'Age of Patient',
            'gender': 'Gender',
            'cancer_type':"Type of Cancer",
            'stage':'Which Stage',
            'diagnosis_date':"When was it First Diagnosed",
            'treatment_type':"Type of Treatment",
            'start_date':"Starting date for Treatment",
            'end_date':'Ending date for Treatment',
            'medication_names':'Medicines Prescibed',
            'eradicated':'Is the Cancer Eradicated?', 
            'recurrence':'Any Signs of Recurrence', 
            'side_effects':'Mention Any Side Effects (NA if None)',
            'quality_of_life_post_treatment':'Quality of Life Post Treatment (out of 10)',
            'direct_costs': 'Total Primary Cost in INR (like Therapy, Medicines etc)', 
            'indirect_costs':'Total Indirect Cost in INR (like Travel to Hospital, Fuel etc)',
                }
