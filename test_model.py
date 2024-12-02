import pandas as pd
import pickle

# Load test data
test_data = pd.read_csv('data/test_data.csv')

# Separate features and labels
X_test = test_data.drop(columns=['label'])
y_test = test_data['label']

# Load model and scaler
with open('model/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
with open('model/scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Align feature names to match the model's expected input
X_test = X_test[scaler.feature_names_in_]

# Scale the test data
X_test_scaled = scaler.transform(X_test)

# Make predictions
y_pred = model.predict(X_test_scaled)

# Output predictions and ground truth
print(f"Predictions: {y_pred}")
print(f"Ground Truth: {y_test.tolist()}")
