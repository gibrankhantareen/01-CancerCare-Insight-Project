from django.db import models

class PatientData(models.Model):
    class Meta:
        unique_together = ['name', 'mobile', 'gender', 'age']

    # Patient details
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    CANCER_TYPE_CHOICES = [
        ('Breast', 'Breast Cancer'),
        ('Lung', 'Lung Cancer'),
        # Add other types as needed
    ]

    ERADICATED_CHOICES = [
    ('YES', 'YES'),
    ('NO', 'NO'),
    ('MAYBE', 'MAYBE'),
    ]

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    mobile = models.CharField(max_length=15, default="0000000000")
    cancer_type = models.CharField(max_length=50, choices=CANCER_TYPE_CHOICES)
    diagnosis_date = models.DateField()

    # Treatment details
    TREATMENT_TYPE_CHOICES = [
        ('Surgery', 'Surgery'),
        ('Chemotherapy', 'Chemotherapy'),
        ('Radiation', 'Radiation'),
        # Add other types as needed
    ]

    # Treatment details
    CANCER_STAGES = [
        ('Stage1', 'Stage 1'),
        ('Stage2', 'Stage 2'),
        ('Stage3', 'Stage 3'),
        ('Stage4', 'Stage 4'),
    ]

    stage = models.CharField(max_length=50, choices=CANCER_STAGES)
    treatment_type = models.CharField(max_length=50, choices=TREATMENT_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    medication_names = models.TextField()  # List down all medications

    # Outcome details
    eradicated = models.CharField(max_length=5, choices=ERADICATED_CHOICES)
    recurrence = models.CharField(max_length=5, choices=ERADICATED_CHOICES)
    side_effects = models.TextField()
    quality_of_life_post_treatment = models.PositiveIntegerField()  # Scale of 1-10

    # Cost details
    direct_costs = models.DecimalField(max_digits=10, decimal_places=2)
    indirect_costs = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    