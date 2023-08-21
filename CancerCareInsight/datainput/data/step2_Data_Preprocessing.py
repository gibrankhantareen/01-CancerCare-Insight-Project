import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder

# Load the dataset
csv_path = "D:/01 CancerCare/CancerCareInsight/datainput/data/final_cancer_data.csv"
data = pd.read_csv(csv_path)

print(data.columns)


# 1. Handle Missing Values
data.dropna(inplace=True)  # Removing rows with missing values for simplicity

# 2. Encoding Categorical Data
categorical_columns = ['Gender', 'Cancer_Type', 'Treatment_Type', 'Eradicated', 'Recurrence', 'Side_Effects']
data = pd.get_dummies(data, columns=categorical_columns, drop_first=True)

# 3. Feature Scaling
scaler = StandardScaler()
numerical_columns = ['Age', 'Direct_Costs', 'Indirect_Costs', 'Quality_of_Life']
data[numerical_columns] = scaler.fit_transform(data[numerical_columns])

# 4. Feature Engineering
# Example: Duration of treatment
data['Treatment_Duration'] = (pd.to_datetime(data['Treatment_End_Date']) - pd.to_datetime(data['Treatment_Start_Date'])).dt.days
data.drop(['Treatment_Start_Date', 'Treatment_End_Date'], axis=1, inplace=True)

# 5. Train-Test Split
# Drop the column using its index
X = data.drop(data.columns[12], axis=1)  # Assuming 'Eradicated' is at index 12
y = data[data.columns[12]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



