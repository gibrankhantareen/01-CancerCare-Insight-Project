from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import pandas as pd


# Load the dataset
csv_path = "D:/01 CancerCare/CancerCareInsight/datainput/data/final_cancer_data.csv"
data = pd.read_csv(csv_path)


# Splitting the data into training and test sets
X = data.drop('Eradicated', axis=1)
y = data['Eradicated']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Identify categorical columns that need to be encoded
categorical_cols = [cname for cname in X_train.columns if 
                    X_train[cname].dtype == "object"]

# Identify numerical columns that need to be scaled
numerical_cols = [cname for cname in X_train.columns if 
                  X_train[cname].dtype in ['int64', 'float64']]

# Preprocessing for numerical data: scale features
numerical_transformer = StandardScaler()

# Preprocessing for categorical data: encode categorical variables
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

# Bundle preprocessing for numerical and categorical data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)])

# Use the ColumnTransformer to apply the transformations to the correct columns in the dataframe
X_train = preprocessor.fit_transform(X_train)
X_test = preprocessor.transform(X_test)




# Initialize the scaler
scaler = StandardScaler()

# Fit the scaler to the training data and transform
X_train_scaled = scaler.fit_transform(X_train)

# Transform the test data
X_test_scaled = scaler.transform(X_test)

