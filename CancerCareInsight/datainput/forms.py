from django import forms
from .models import PatientData

class PatientDataForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))
    medication_names = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}))
    eradicated = forms.ChoiceField(choices=[('YES', 'YES'), ('NO', 'NO'), ('MAYBE', 'MAYBE')])
    recurrence = forms.ChoiceField(choices=[('YES', 'YES'), ('NO', 'NO'), ('MAYBE', 'MAYBE')])
    diagnosis_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    side_effects = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}))
    

    class Meta:
        model = PatientData
        fields = [
            'name', 'age', 'gender', 'mobile', 'cancer_type', 'stage', 'diagnosis_date',
            'treatment_type', 'start_date', 'end_date', 'medication_names',
            'eradicated', 'recurrence', 'side_effects', 'quality_of_life_post_treatment',
            'direct_costs', 'indirect_costs'
        ]

    
        labels = {
            'name': 'Full Name',
            'age': 'Age of Patient',
            'gender': 'Gender',
            'mobile': 'Enter Mobile Number (+91)',
            'cancer_type': 'Type of Cancer',
            'stage': 'Which Stage?',
            'diagnosis_date': 'When was it Diagnosed',
            'treatment_type': 'Type of Treatment',
            'start_date': 'Starting date for Treatment',
            'end_date': 'Ending date for Treatment',
            'medication_names': 'Medicines Prescibed',
            'eradicated': 'Is the Cancer Eradicated?', 
            'recurrence': 'Any Signs of Recurrence', 
            'side_effects': 'Mention Any Side Effects (NA if None)',
            'quality_of_life_post_treatment': 'Quality of Life Post Treatment (out of 10)',
            'direct_costs': 'Total Primary Cost in INR (like Therapy, Medicines etc)', 
            'indirect_costs': 'Total Indirect Cost in INR (like Travel to Hospital, Fuel etc)',
            }
        
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        mobile = cleaned_data.get('mobile')
        gender = cleaned_data.get('gender')
        age = cleaned_data.get('age')

        if PatientData.objects.filter(name=name, mobile=mobile, gender=gender, age=age).exists():
            raise forms.ValidationError("Duplicate entry detected. Please check the details.")
        return cleaned_data
