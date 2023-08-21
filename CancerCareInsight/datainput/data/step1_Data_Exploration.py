# Import necessary libraries
import pandas as pd

# Load the dataset
csv_path = "D:/01 CancerCare/CancerCareInsight/datainput/data/final_cancer_data.csv"
data = pd.read_csv(csv_path)

# Display the first few rows of the dataset
print(data.head())

# Check the data types of each column
print(data.dtypes)

# Generate summary statistics for numerical columns
print(data.describe())

# Check the distribution of categorical columns
categorical_columns = ['Name', 'Gender', 'City', 'Cancer_Type', 'Treatment_Type', 'Stage', 'Medication_Names', 'Eradicated', 'Recurrence', 'Side_Effects']
for column in categorical_columns:
    print(data[column].value_counts())

# Check for missing values in the dataset
print(data.isnull().sum())

# Import necessary libraries for visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Distribution Plots for Age, Direct_Costs, and Indirect_Costs
for column in ['Age', 'Direct_Costs', 'Indirect_Costs']:
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], kde=True)
    plt.title(f'Distribution of {column}')
    plt.show()

# Bar Plots for Gender, Cancer_Type, and Treatment_Type
for column in ['Gender', 'Cancer_Type', 'Treatment_Type']:
    plt.figure(figsize=(10, 6))
    sns.countplot(y=data[column])  # Using y instead of x
    plt.title(f'Distribution of {column}')
    plt.xticks(rotation=45)
    plt.show()


# Box Plots for Age and Costs
for column in ['Age', 'Direct_Costs', 'Indirect_Costs']:
    plt.figure(figsize=(10, 6))
    sns.boxplot(data[column])
    plt.title(f'Box Plot of {column}')
    plt.show()

# Correlation Matrix for numerical columns
correlation_matrix = data[['Age', 'Direct_Costs', 'Indirect_Costs']].corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
