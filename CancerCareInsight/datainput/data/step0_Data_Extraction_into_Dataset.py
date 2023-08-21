import pandas as pd
import random
from datetime import datetime, timedelta

# Number of records
N = 10000

# Names
first_names = ["Amit", "Rohit", "Priya", "Anjali", "Suresh", "Ramesh", "Geeta", "Rekha", "Raj", "Simran"]
last_names = ["Sharma", "Verma", "Patel", "Kumar", "Singh", "Gupta", "Dixit", "Jain", "Agarwal", "Malhotra"]

# Age
def generate_age():
    if random.random() < 0.1:
        return random.randint(0, 10)
    return random.randint(20, 90)

# Gender
genders = ["Male", "Female"]

# Mobile
def generate_mobile():
    return "9" + "".join([str(random.randint(0, 9)) for _ in range(9)])

# Cancer Type
cancer_types = ["Breast", "Lung", "Prostate", "Colorectal", "Leukemia", "Liver", "Stomach", "Cervical", "Thyroid", "Bladder"]

# Diagnosis Date
def generate_date():
    end = datetime.now()
    start = end - timedelta(days=10*365)
    return start + (end - start) * random.random()

# Treatment
treatments = ["Surgery", "Chemotherapy", "Radiation"]

# Stage
stages = [1, 2, 3, 4]

# Medication Names
medications = ["Tamoxifen", "Methotrexate", "Cisplatin", "Carboplatin", "Letrozole", "Rituximab", "Pembrolizumab", "Trastuzumab"]

# Eradicated & Recurrence
eradicated_options = ["YES", "NO", "MAYBE"]
recurrence_options = ["YES", "NO", "MAYBE"]

# Side Effects
side_effects = ["Fatigue", "Pain", "Nausea", "Hair Loss", "Anemia", "Infections", "Appetite Changes"]

# Quality of Life
def quality_of_life():
    return random.randint(1, 10)

# Direct Costs based on city
cities = ["Bengaluru", "New Delhi", "Mumbai", "Gurgaon", "Chennai", "Hyderabad"]
costs = {
    "Bengaluru": (112000, 3500000),
    "New Delhi": (130000, 5050000),
    "Mumbai": (150000, 4050000),
    "Gurgaon": (112000, 3500000),
    "Chennai": (110000, 4510000),
    "Hyderabad": (112000, 3500000)
}

def generate_cost(city):
    return random.randint(costs[city][0], costs[city][1])

# Indirect Costs
def indirect_cost(direct_cost):
    return int(direct_cost * random.uniform(0.2, 0.3))

# Generate dataset
data = []
for _ in range(N):
    name = random.choice(first_names) + " " + random.choice(last_names)
    age = generate_age()
    gender = random.choice(genders)
    city = random.choice(cities)
    mobile = generate_mobile()
    cancer_type = random.choice(cancer_types)
    diagnosis_date = generate_date()
    treatment = random.choice(treatments)
    treatment_start_date = generate_date()
    treatment_end_date = treatment_start_date + timedelta(days=random.randint(30, 180))
    stage = random.choice(stages)
    medication = random.choice(medications)
    eradicated = random.choice(eradicated_options)
    recurrence = random.choice(recurrence_options)
    side_effect = random.choice(side_effects)
    quality = quality_of_life()
    direct_cost = generate_cost(city)
    indirect = indirect_cost(direct_cost)
    
    data.append([name, age, gender, city, mobile, cancer_type, diagnosis_date, treatment, treatment_start_date, treatment_end_date, stage, medication, eradicated, recurrence, side_effect, quality, direct_cost, indirect])

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Name", "Age", "Gender", "City", "Mobile", "Cancer Type", "Diagnosis Date", "Treatment", "Treatment Start Date", "Treatment End Date", "Stage", "Medication", "Eradicated", "Recurrence", "Side Effect", "Quality of Life", "Direct Cost", "Indirect Cost"])

# Save to CSV
df.to_csv("synthetic_cancer_data.csv", index=False)

print("Dataset generated and saved to 'synthetic_cancer_data.csv'")
