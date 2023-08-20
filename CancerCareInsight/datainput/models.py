from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    CANCER_TYPE_CHOICES = [
        ('Breast', 'Breast Cancer'),
        ('Lung', 'Lung Cancer'),
        # Add other types as needed
    ]

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    cancer_type = models.CharField(max_length=50, choices=CANCER_TYPE_CHOICES)
    stage = models.PositiveIntegerField()
    diagnosis_date = models.DateField()


class Treatment(models.Model):
    TREATMENT_TYPE_CHOICES = [
        ('Surgery', 'Surgery'),
        ('Chemotherapy', 'Chemotherapy'),
        ('Radiation', 'Radiation'),
        # Add other types as needed
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    treatment_type = models.CharField(max_length=50, choices=TREATMENT_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    medication_names = models.TextField()  # List down all medications



class Outcome(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    eradicated = models.BooleanField()
    recurrence = models.BooleanField()
    side_effects = models.TextField()
    quality_of_life_post_treatment = models.PositiveIntegerField()  # Scale of 1-10



class Cost(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    direct_costs = models.DecimalField(max_digits=10, decimal_places=2)
    indirect_costs = models.DecimalField(max_digits=10, decimal_places=2)

